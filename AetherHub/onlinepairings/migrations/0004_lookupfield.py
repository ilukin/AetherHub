# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinepairings', '0003_player'),
    ]

    operations = [
        migrations.CreateModel(
            name='LookupField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lookup_value_DCI', models.CharField(blank=True, max_length=10)),
                ('lookup_value_table', models.CharField(blank=True, max_length=4)),
            ],
        ),
    ]
