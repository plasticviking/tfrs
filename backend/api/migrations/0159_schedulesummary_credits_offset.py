# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-16 20:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0158_auto_20190716_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedulesummary',
            name='credits_offset',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
