from django.db import models

from api.models.CompliancePeriod import CompliancePeriod
from api.models.DocumentStatus import DocumentStatus
from api.models.DocumentType import DocumentType


class DocumentData(models.Model):
    """Common fields for Document and DocumentHistory"""

    title = models.CharField(
        max_length=120
    )

    status = models.ForeignKey(
        DocumentStatus,
        on_delete=models.PROTECT,
        null=False
    )

    type = models.ForeignKey(
        DocumentType,
        on_delete=models.PROTECT,
        null=False
    )

    compliance_period = models.ForeignKey(
        CompliancePeriod,
        on_delete=models.PROTECT,
        null=False
    )

    record_number = models.CharField(
        blank=True, max_length=100, null=True,
        db_comment='Number stored in TRIM'
    )

    class Meta:
        abstract = True
