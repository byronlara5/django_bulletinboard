# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-06 17:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0023_auto_20180306_1141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enhorabuenakid',
            name='title',
        ),
    ]
