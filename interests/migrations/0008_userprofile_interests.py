# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-24 07:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interests', '0007_auto_20170420_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='interests',
            field=models.ManyToManyField(to='interests.Interest'),
        ),
    ]
