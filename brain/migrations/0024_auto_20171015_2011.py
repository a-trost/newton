# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-15 20:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('brain', '0023_auto_20171011_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataupdate',
            name='dateandtime',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 15, 16, 11, 5, 831574, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='readingtimespent',
            name='time_spent',
            field=models.IntegerField(default=0, verbose_name='Seconds Spent Reading'),
        ),
    ]
