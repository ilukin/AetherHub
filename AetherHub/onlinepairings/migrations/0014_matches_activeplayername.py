# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-04 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinepairings', '0013_controls_seatings'),
    ]

    operations = [
        migrations.AddField(
            model_name='matches',
            name='activePlayerName',
            field=models.CharField(default='loremipsum', max_length=75),
            preserve_default=False,
        ),
    ]
