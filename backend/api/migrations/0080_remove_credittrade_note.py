# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-19 20:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0079_auto_20190219_1859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='credittrade',
            name='note',
        ),
    ]
