# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-06 19:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0025_enhorabuenakid_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='url',
            field=models.CharField(default='none', max_length=80),
        ),
    ]
