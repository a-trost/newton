# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-09 13:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('brain', '0020_auto_20171009_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataupdate',
            name='dateandtime',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 9, 9, 11, 15, 4892, tzinfo=utc)),
        ),
    ]
