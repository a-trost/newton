# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-19 23:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('brain', '0025_auto_20171015_2011'),
    ]

    operations = [
        migrations.CreateModel(
            name='StreakHighScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_achieved', models.DateField(default=datetime.date.today, verbose_name='Date Read')),
                ('days_in_a_row', models.IntegerField(default=1, verbose_name='Days in a row')),
                ('site', models.CharField(choices=[('IXL', 'IXL'), ('MYON', 'MYON'), ('RAZKIDS', 'RAZKIDS'), ('REMIND', 'REMIND')], max_length=100)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brain.StudentRoster')),
            ],
        ),
        migrations.AlterField(
            model_name='dataupdate',
            name='dateandtime',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 19, 19, 22, 1, 987898, tzinfo=utc)),
        ),
    ]
