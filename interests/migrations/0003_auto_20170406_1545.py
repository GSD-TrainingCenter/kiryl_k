# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interests', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]