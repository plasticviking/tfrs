import json
from collections import namedtuple
from decimal import Decimal

from django.db.models import Q

from api.models.ComplianceReport import ComplianceReport, ComplianceReportWorkflowState, ComplianceReportStatus
from api.models.ComplianceReportHistory import ComplianceReportHistory
from api.models.CreditTrade import CreditTrade
from api.models.CreditTradeStatus import CreditTradeStatus
from api.models.CreditTradeType import CreditTradeType
from api.models.Organization import Organization
from api.services.CreditTradeService import CreditTradeService

Delta = namedtuple('Delta', ['path', 'field', 'action', 'old_value', 'new_value'])


class ComplianceReportService(object):
    """
    Helper functions for Compliance Reporting
    """

    def _array_difference(ancestor, current, field, path, i=0):
        longest = max(len(ancestor[field]), len(current[field]))

        if i >= longest:
            return []

        if i >= len(current[field]):
            return [
                       Delta(path='.'.join(path),
                             field='{}[{}]'.format(field, i),
                             action='removed',
                             old_value=ancestor[field][i],
                             new_value=None)._asdict()
                   ] + ComplianceReportService._array_difference(ancestor, current, field, path, i + 1)

        if i >= len(ancestor[field]):
            return [
                       Delta(path='.'.join(path),
                             field='{}[{}]'.format(field, i),
                             action='added',
                             old_value=None,
                             new_value=current[field][i])._asdict()
                   ] + ComplianceReportService._array_difference(ancestor, current, field, path, i + 1)

        if isinstance(current[field][i], dict):
            comparison = ComplianceReportService.compute_delta(current[field][i],
                                                               ancestor[field][i],
                                                               path=path + ['{}[{}]'.format(field, i)])

            return comparison + ComplianceReportService._array_difference(ancestor, current, field, path, i + 1)

        if str(current[field][i]) != str(ancestor[field][i]):
            return [
                       Delta(path='.'.join(path),
                             field='{}[{}]'.format(field, i),
                             action='modified',
                             old_value=ancestor[field][i],
                             new_value=current[field][i])._asdict()
                   ] + ComplianceReportService._array_difference(ancestor, current, field, path, i + 1)

        return ComplianceReportService._array_difference(ancestor, current, field, path, i + 1)

    @staticmethod
    def compute_delta(snapshot, ancestor_snapshot, path=[]):

        differences = []
        blacklist_keys = ['id', 'timestamp', 'status', 'read_only', 'actions', 'version', 'timestamp']

        for k in snapshot.keys():
            if k in blacklist_keys:
                continue
            current_path = path + [k]
            if k in ancestor_snapshot:
                if k not in ancestor_snapshot:
                    differences += [Delta(path='.'.join(path),
                                        field=k,
                                        action='added',
                                        old_value=None,
                                        new_value=snapshot[k])._asdict()]
                    continue
                if isinstance(snapshot[k], dict):
                    comparison = ComplianceReportService.compute_delta(snapshot[k],
                                                                       ancestor_snapshot[k],
                                                                       path=current_path)
                    if len(comparison) > 0:
                        differences += comparison
                    continue
                if isinstance(snapshot[k], list):
                    differences += ComplianceReportService._array_difference(ancestor_snapshot, snapshot, k, path)
                    continue
                if str(snapshot[k]) != str(ancestor_snapshot[k]):
                    differences += [Delta(path='.'.join(path),
                                         field=k,
                                         action='modified',
                                         old_value=ancestor_snapshot[k],
                                         new_value=snapshot[k])._asdict()]

        for k in ancestor_snapshot.keys():
            if k in blacklist_keys:
                continue
            if k not in snapshot:
                differences += [Delta(path='.'.join(path),
                                      field=k,
                                      action='removed',
                                      old_value=ancestor_snapshot[k],
                                      new_value=None)._asdict()]

        return differences

    @staticmethod
    def get_organization_compliance_reports(organization):
        """
        Fetch the compliance reports with various rules based on the user's
        organization
        """
        # Government Organization -- assume OrganizationType id 1 is gov
        gov_org = Organization.objects.get(type=1)

        if organization == gov_org:
            # If organization == Government
            #  don't show "Draft" transactions
            #  don't show "Deleted" transactions
            compliance_reports = ComplianceReport.objects.filter(
                ~Q(status__fuel_supplier_status__status__in=["Draft", "Deleted"])
            )
        else:
            # If organization == Fuel Supplier
            # Show all compliance reports for which we are the organization
            compliance_reports = ComplianceReport.objects.filter(
                Q(organization=organization) &
                ~Q(status__fuel_supplier_status__status__in=["Deleted"])
            )

        return compliance_reports

    @staticmethod
    def create_history(compliance_report, is_new=False):
        """
        Create the CreditTradeHistory
        """
        user = (
            compliance_report.create_user
            if is_new or compliance_report.update_user is None
            else compliance_report.update_user)

        role_id = None

        if user:
            if user.roles.filter(name="GovDirector").exists():
                role_id = user.roles.get(name="GovDirector").id
            elif user.roles.filter(name="GovDeputyDirector").exists():
                role_id = user.roles.get(name="GovDeputyDirector").id
            else:
                role_id = user.roles.first().id

        created_status = ComplianceReportWorkflowState.objects.create(
            fuel_supplier_status=compliance_report.status.fuel_supplier_status,
            analyst_status=compliance_report.status.analyst_status,
            manager_status=compliance_report.status.manager_status,
            director_status=compliance_report.status.director_status
        )
        created_status.save()

        history = ComplianceReportHistory(
            compliance_report_id=compliance_report.id,
            status_id=created_status.id,
            create_user=user,
            user_role_id=role_id
        )

        history.save()

    @staticmethod
    def create_director_transactions(compliance_report, creating_user):
        """
        Validate or Reduce credits when the director accepts a compliance report

        Always use the snapshot as the basis for calculation, so we don't
        recompute anything and possibly alter the values

        :param compliance_report:
        :return:
        """
        if compliance_report.snapshot is None:
            raise InvalidStateException()

        snapshot = compliance_report.snapshot

        if 'summary' not in snapshot:
            raise InvalidStateException()
        if 'lines' not in snapshot['summary']:
            raise InvalidStateException()

        lines = snapshot['summary']['lines']

        if Decimal(lines['25']) > Decimal(0):
            # do validation for Decimal(lines['25'])
            credit_transaction = CreditTrade(
                initiator=Organization.objects.get(id=1),
                respondent=compliance_report.organization,
                status=CreditTradeStatus.objects.get(status='Draft'),
                type=CreditTradeType.objects.get(the_type='Credit Validation'),
                number_of_credits=Decimal(lines['25']),
                compliance_period=compliance_report.compliance_period,
                create_user=creating_user,
                update_user=creating_user
            )
            credit_transaction.save()
            credit_transaction.refresh_from_db()
            CreditTradeService.approve(credit_transaction)
            compliance_report.credit_transaction = credit_transaction
            compliance_report.save()
            CreditTradeService.pvr_notification(None, credit_transaction)
        else:
            if Decimal(lines['25']) < 0 and Decimal(lines['26']) > Decimal(0):
                # do_reduction for Decimal(lines['26'])
                credit_transaction = CreditTrade(
                    initiator=Organization.objects.get(id=1),
                    respondent=compliance_report.organization,
                    status=CreditTradeStatus.objects.get(status='Draft'),
                    type=CreditTradeType.objects.get(the_type='Credit Reduction'),
                    number_of_credits=Decimal(lines['26']),
                    compliance_period=compliance_report.compliance_period,
                    create_user=creating_user,
                    update_user=creating_user
                )
                credit_transaction.save()
                credit_transaction.refresh_from_db()
                CreditTradeService.approve(credit_transaction)
                compliance_report.credit_transaction = credit_transaction
                compliance_report.save()
                CreditTradeService.pvr_notification(None, credit_transaction)


class InvalidStateException(Exception):
    """
    Used to indicate that the compliance report is not in a state we can
    generate a PVR from (missing data, wrong version, etc.)
    """
    pass
