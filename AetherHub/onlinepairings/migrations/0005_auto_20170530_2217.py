# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 20:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinepairings', '0004_lookupfield'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lookupfield',
            name='lookup_value_table',
        ),
        migrations.AlterField(
            model_name='lookupfield',
            name='lookup_value_DCI',
            field=models.CharField(max_length=10),
        ),
    ]