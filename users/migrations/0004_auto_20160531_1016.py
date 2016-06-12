# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 02:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20160531_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oauth',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
