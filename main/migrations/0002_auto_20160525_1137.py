# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-05-25 08:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='foto',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Album', verbose_name='\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430 \u0438\u043b\u0438 \u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u043e\u0432\u043e\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435:'),
        ),
        migrations.AlterField(
            model_name='foto',
            name='foto',
            field=models.ImageField(upload_to='fotos/thumbnails/%Y/%m/%d', verbose_name='\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0444\u043e\u0442\u043e\u0444\u0430\u0439\u043b'),
        ),
    ]