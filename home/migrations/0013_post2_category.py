# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-06 11:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20180106_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='post2',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.category'),
            preserve_default=False,
        ),
    ]