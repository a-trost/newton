# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-19 02:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('brain', '0038_auto_20171113_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataupdate',
            name='dateandtime',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 18, 21, 5, 33, 276234, tzinfo=utc)),
        ),
    ]
