# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-10 17:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0030_auto_20180410_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='memorandum',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
