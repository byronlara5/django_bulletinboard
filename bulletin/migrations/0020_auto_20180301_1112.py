# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-01 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0019_enhorabuenakid_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enhorabuenakid',
            name='thumb',
            field=models.ImageField(default='', editable=False, upload_to='photos/%Y/%m/%d'),
        ),
    ]
