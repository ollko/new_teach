# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-10-13 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oge', '0003_useranswer_res_numbers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswer',
            name='res',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='\u0447\u0438\u0441\u043b\u043e \u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u044b\u0445 \u043e\u0442\u0432\u0435\u0442\u043e\u0432'),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='user_answer',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='\u0441\u0442\u0440\u043e\u043a\u0430 \u0441 \u043e\u0442\u0432\u0435\u0442\u0430\u043c\u0438 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f'),
        ),
    ]
