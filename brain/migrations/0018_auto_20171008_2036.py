# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-08 20:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('brain', '0017_auto_20171005_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataupdate',
            name='dateandtime',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 8, 16, 36, 5, 565889, tzinfo=utc)),
        ),
    ]
