# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-06-30 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160525_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='foto',
            name='foto_1x',
            field=models.ImageField(default=None, null=True, upload_to='fotos/thumbnails/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='foto',
            name='foto_2x',
            field=models.ImageField(default=None, null=True, upload_to='fotos/thumbnails/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='foto',
            name='foto_3x',
            field=models.ImageField(default=None, null=True, upload_to='fotos/thumbnails/%Y/%m/%d'),
        ),
    ]
