# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-05 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20180105_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='post3',
            name='content',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
