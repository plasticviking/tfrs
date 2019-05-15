# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-14 17:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0129_auto_20190513_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='autosavedformdata',
            name='last_access',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='last_access'),
        ),
    ]