# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 18:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinepairings', '0006_auto_20170531_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='Otable',
            field=models.CharField(default=0, max_length=4),
        ),
    ]