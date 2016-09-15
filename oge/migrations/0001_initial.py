# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-09-13 10:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tests18_26',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tests18_26', models.TextField()),
                ('splited_tests18_26', models.TextField(blank=True, default=None, null=True)),
                ('pub_data', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u0434\u0430\u0442\u0430 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438')),
                ('answer', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('qw_number', models.CharField(default='9', max_length=1, null=True, verbose_name='\u0447\u0438\u0441\u043b\u043e \u0432\u043e\u043f\u0440\u043e\u0441\u043e\u0432 \u0432 \u0442\u0435\u0441\u0442\u0435')),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_answer', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('res', models.IntegerField(blank=True, default=None, null=True)),
                ('res_numbers', models.CharField(blank=True, default=None, max_length=9, null=True, verbose_name='\u0441\u0442\u0440\u043e\u043a\u0430 \u043e\u0442\u0432\u0435\u0442\u043e\u0432 \u0438\u0437 0 \u0438 1')),
                ('answer_pub_data', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u0434\u0430\u0442\u0430 \u043e\u0442\u0432\u0435\u0442\u0430')),
                ('test18_26', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oge.Tests18_26')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
