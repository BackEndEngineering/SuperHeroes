# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 21:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('HeroSandwich', '0006_auto_20160518_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='age',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 18, 21, 45, 41, 86158, tzinfo=utc), verbose_name='Born'),
            preserve_default=False,
        ),
    ]