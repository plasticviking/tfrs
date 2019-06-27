# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-27 23:17
from __future__ import unicode_literals

import api.models.ComplianceReportSchedules
from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0151_rename_table_sequences'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'compliance_report_schedule_d',
            },
        ),
        migrations.CreateModel(
            name='ScheduleDSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedstock', models.CharField(blank=True, max_length=100, null=True)),
                ('fuel_class', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.FuelClass')),
                ('fuel_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.ApprovedFuel')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sheets', to='api.ScheduleD')),
            ],
            options={
                'db_table': 'compliance_report_schedule_d_sheet',
            },
        ),
        migrations.CreateModel(
            name='ScheduleDSheetInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worksheet_name', models.CharField(blank=True, max_length=100, null=True)),
                ('cell', models.CharField(blank=True, max_length=100, null=True)),
                ('value', models.CharField(blank=True, max_length=100, null=True)),
                ('units', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('sheet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='inputs', to='api.ScheduleDSheet')),
            ],
            options={
                'db_table': 'compliance_report_schedule_d_sheet_input',
            },
        ),
        migrations.CreateModel(
            name='ScheduleDSheetOutput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intensity', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=5, null=True)),
                ('description', models.CharField(blank=True, choices=[(api.models.ComplianceReportSchedules.ScheduleDSheetOutput.OutputCells('Fuel Dispensing'), 'DISPENSING'), (api.models.ComplianceReportSchedules.ScheduleDSheetOutput.OutputCells('Fuel Distribution and Storage'), 'DISTRIBUTION'), (api.models.ComplianceReportSchedules.ScheduleDSheetOutput.OutputCells('Fuel Production'), 'PRODUCTION'), (api.models.ComplianceReportSchedules.ScheduleDSheetOutput.OutputCells('Feedstock Transmission'), 'FEEDSTOCK_TRANSMISSION'), (api.models.ComplianceReportSchedules.ScheduleDSheetOutput.OutputCells('Feedstock Recovery'), 'FEEDSTOCK_RECOVERY'), (api.models.ComplianceReportSchedules.ScheduleDSheetOutput.OutputCells('Feedstock Upgrading'), 'FEEDSTOCK_UPGRADING'), (api.models.ComplianceReportSchedules.ScheduleDSheetOutput.OutputCells('Land Use Change'), 'LAND_USE_CHANGE'), (api.models.ComplianceReportSchedules.ScheduleDSheetOutput.OutputCells('Fertilizer Manufacture'), 'FERTILIZER'), (api.models.ComplianceReportSchedules.ScheduleDSheetOutput.OutputCells('Gas Leaks and Flares'), 'GAS_LEAKS_AND_FLARES'), (api.models.ComplianceReportSchedules.ScheduleDSheetOutput.OutputCells('CO₂ and H₂S Removed'), 'CO2_AND_H2S_REMOVED'), (api.models.ComplianceReportSchedules.ScheduleDSheetOutput.OutputCells('Emissions Displaced'), 'EMISSIONS_DISPLACED'), (api.models.ComplianceReportSchedules.ScheduleDSheetOutput.OutputCells('Fuel Use (High Heating Value)'), 'FUEL_USE_HIGH_HEATING_VALUE')], max_length=100, null=True)),
                ('sheet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='outputs', to='api.ScheduleDSheet')),
            ],
            options={
                'db_table': 'compliance_report_schedule_d_sheet_output',
            },
        ),
        migrations.AddField(
            model_name='compliancereport',
            name='schedule_d',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='compliance_report', to='api.ScheduleD'),
        ),
        migrations.AlterUniqueTogether(
            name='scheduledsheetoutput',
            unique_together=set([('description', 'sheet')]),
        ),
    ]