# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-21 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0013_auto_20180220_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetpartner',
            name='thumb',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d'),
        ),
    ]
