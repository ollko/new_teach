# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-10-10 17:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mom', '0002_auto_20171010_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stuff',
            name='post',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0438 \u0434\u0430\u0442\u0430 \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0438'),
        ),
    ]
