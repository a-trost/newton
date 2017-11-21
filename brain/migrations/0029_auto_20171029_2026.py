# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-29 20:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('brain', '0028_auto_20171029_2018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teachersettings',
            name='bonus_exercises',
        ),
        migrations.RemoveField(
            model_name='teachersettings',
            name='cba_exercises',
        ),
        migrations.RemoveField(
            model_name='teachersettings',
            name='mastery_exercises',
        ),
        migrations.RemoveField(
            model_name='teachersettings',
            name='nwea_exercises',
        ),
        migrations.AlterField(
            model_name='dataupdate',
            name='dateandtime',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 29, 16, 26, 45, 550684, tzinfo=utc)),
        ),
    ]
