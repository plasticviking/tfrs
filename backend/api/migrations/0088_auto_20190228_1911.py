# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-28 19:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0087_add_fuel_code_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuelcode',
            name='carbon_intensity',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True),
        ),
    ]
