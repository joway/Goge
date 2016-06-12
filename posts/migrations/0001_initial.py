# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 06:41
from __future__ import unicode_literals

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.CharField(default=posts.models.post_unique_uuid, editable=False, max_length=12, primary_key=True, serialize=False, verbose_name='uuid')),
                ('author', models.CharField(max_length=16)),
                ('title', models.CharField(max_length=32)),
                ('content', models.TextField(blank=True)),
                ('url', models.URLField(verbose_name='链接')),
                ('score', models.IntegerField(default=0, verbose_name='评分')),
                ('create_at', models.DateTimeField(blank=True, null=True)),
                ('last_scanned', models.DateTimeField()),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, '已更新'), (1, '待更新'), (2, '不活跃'), (-1, '404 死链')])),
            ],
        ),
    ]
