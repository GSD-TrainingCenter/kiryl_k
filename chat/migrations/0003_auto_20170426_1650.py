# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-26 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20170420_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='message',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
