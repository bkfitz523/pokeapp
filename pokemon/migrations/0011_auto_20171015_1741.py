# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-15 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0010_auto_20171015_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='move',
            name='contest',
            field=models.CharField(default='Cool', max_length=50),
        ),
        migrations.AlterField(
            model_name='move',
            name='category',
            field=models.CharField(default='Physical', max_length=50),
        ),
    ]
