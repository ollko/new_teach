# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-09-19 11:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='birth_data',
            field=models.DateField(default=datetime.date(2017, 9, 19)),
        ),
        migrations.AddField(
            model_name='join',
            name='check_in_date',
            field=models.CharField(default='24\u201326.11.17', max_length=15),
        ),
        migrations.AddField(
            model_name='join',
            name='child_name',
            field=models.CharField(default='\u0418\u0432\u0430\u043d\u043e\u0432 \u0418\u0432\u0430\u043d \u0418\u0432\u0430\u043d\u043e\u0432\u0438\u0447', max_length=100),
        ),
        migrations.AddField(
            model_name='join',
            name='parents_name',
            field=models.CharField(default='\u0418\u0432\u0430\u043d\u043e\u0432 \u0418\u0432\u0430\u043d \u0418\u0432\u0430\u043d\u043e\u0432\u0438\u0447', max_length=100),
        ),
        migrations.AddField(
            model_name='join',
            name='tel',
            field=models.CharField(default='1234567890', max_length=10),
        ),
    ]
