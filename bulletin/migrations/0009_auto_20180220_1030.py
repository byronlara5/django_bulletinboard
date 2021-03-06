# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-20 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0008_birthdays'),
    ]

    operations = [
        migrations.CreateModel(
            name='Birthday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('department', models.CharField(max_length=80)),
                ('allDay', models.BooleanField(default=True)),
                ('start_date', models.DateField(null=True)),
                ('start_time', models.TimeField(auto_now=True)),
                ('end_date', models.DateField(null=True)),
                ('end_time', models.TimeField(auto_now=True)),
                ('backgroundColor', models.CharField(default='#1b9200', max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('picture', models.ImageField(null=True, upload_to='photos/%Y/%m/%d')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Welcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('picture', models.ImageField(null=True, upload_to='photos/%Y/%m/%d')),
                ('text', models.TextField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Events',
            new_name='Event',
        ),
        migrations.RenameModel(
            old_name='Memorandums',
            new_name='Memorandum',
        ),
        migrations.RenameModel(
            old_name='QuotesDay',
            new_name='Quote',
        ),
        migrations.DeleteModel(
            name='Birthdays',
        ),
    ]
