# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-30 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calender', '0002_auto_20170130_1341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calender',
            old_name='end',
            new_name='end_date',
        ),
        migrations.RenameField(
            model_name='calender',
            old_name='start',
            new_name='start_date',
        ),
        migrations.AddField(
            model_name='calender',
            name='end_time',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='calender',
            name='start_time',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
