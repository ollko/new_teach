# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-10-13 07:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u0410\u0432\u0442\u043e\u0440 \u0441\u0442\u0430\u0442\u044c\u0438'),
        ),
    ]