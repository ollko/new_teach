# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-11-29 11:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album', models.CharField(max_length=200, unique=True)),
                ('album_date', models.DateField(verbose_name='album date')),
                ('views', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='fotos/%Y/%m', verbose_name='\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0444\u043e\u0442\u043e\u0444\u0430\u0439\u043b')),
                ('foto_1x', models.ImageField(default=None, null=True, upload_to='fotos/%Y/%m')),
                ('foto_2x', models.ImageField(default=None, null=True, upload_to='fotos/%Y/%m')),
                ('foto_3x', models.ImageField(default=None, null=True, upload_to='fotos/%Y/%m')),
                ('published_date', models.DateField()),
                ('likes', models.IntegerField(default=0)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Album', verbose_name='\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430 \u0438\u043b\u0438 \u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u043e\u0432\u043e\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435:')),
            ],
        ),
    ]
