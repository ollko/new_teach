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
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('video_html_code', models.CharField(default=None, max_length=200, verbose_name='html-\u043a\u043e\u0434')),
                ('pub_date', models.DateTimeField()),
                ('youtube_id', models.CharField(blank=True, default=None, max_length=11, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VideoSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, unique=True, verbose_name='\u0440\u0430\u0437\u0434\u0435\u043b \u0432\u0438\u0434\u0435\u043e')),
            ],
        ),
        migrations.AddField(
            model_name='video',
            name='video_section',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='videos.VideoSection', verbose_name='\u0440\u0430\u0437\u0434\u0435\u043b'),
        ),
    ]
