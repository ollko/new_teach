# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-09-15 10:40
from __future__ import unicode_literals

import baner.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Baner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=220)),
                ('title_description', models.TextField(blank=True, null=True)),
                ('title_btn', models.CharField(default='Join', max_length=50)),
                ('title_btn_url', models.CharField(default='Join', max_length=50)),
                ('content1', models.TextField(blank=True, null=True)),
                ('content2', models.TextField(blank=True, null=True)),
                ('content3', models.TextField(blank=True, null=True)),
                ('content4', models.TextField(blank=True, null=True)),
                ('content5', models.TextField(blank=True, null=True)),
                ('content6', models.TextField(blank=True, null=True)),
                ('content_bg_color', models.CharField(default='#000000', max_length=7, validators=[baner.models.layout_validator])),
                ('video_embed', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, default='page-slug')),
                ('featured', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('leave_capture', models.BooleanField(default=True)),
            ],
        ),
    ]
