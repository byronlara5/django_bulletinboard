# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-11 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0033_auto_20180411_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='allDay',
            field=models.BooleanField(default=False, editable=False, verbose_name='Todo el dia'),
        ),
    ]
