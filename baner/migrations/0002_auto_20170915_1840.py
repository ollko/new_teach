# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-09-15 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baner', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='baner',
            old_name='content_bg_color',
            new_name='jumbotron_bg_color',
        ),
        migrations.AddField(
            model_name='baner',
            name='jumbotron_bg_img',
            field=models.ImageField(blank=True, null=True, upload_to='baner'),
        ),
    ]
