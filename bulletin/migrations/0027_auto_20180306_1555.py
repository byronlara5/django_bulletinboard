# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-06 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0026_event_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='url',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
