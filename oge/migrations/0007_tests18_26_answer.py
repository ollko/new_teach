# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-08-24 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oge', '0006_remove_tests18_26_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='tests18_26',
            name='answer',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
