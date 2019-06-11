# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-04 17:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0138_auto_20190530_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='provisionoftheact',
            name='display_order',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='provisionoftheact',
            name='effective_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='provisionoftheact',
            name='expiration_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='provisionoftheact',
            name='determination_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='fuel_provision', to='api.CarbonIntensityDeterminationType'),
        ),
        migrations.AlterModelTable(
            name='carbonintensitydeterminationtype',
            table='determination_type',
        ),
        migrations.AlterModelTable(
            name='provisionoftheact',
            table='fuel_provision',
        ),
    ]
