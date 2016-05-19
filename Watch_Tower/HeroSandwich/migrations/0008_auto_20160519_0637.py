# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 06:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('HeroSandwich', '0007_character_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='First_Appearance',
            field=models.CharField(default=datetime.datetime(2016, 5, 19, 6, 35, 50, 415539, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='eye_color',
            field=models.CharField(default=datetime.datetime(2016, 5, 19, 6, 36, 8, 779145, tzinfo=utc), max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='hair_color',
            field=models.CharField(default=datetime.datetime(2016, 5, 19, 6, 36, 32, 587040, tzinfo=utc), max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='height',
            field=models.PositiveIntegerField(default=0, verbose_name='Height'),
        ),
        migrations.AddField(
            model_name='character',
            name='powers_weapons',
            field=models.CharField(default=datetime.datetime(2016, 5, 19, 6, 36, 53, 282730, tzinfo=utc), max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='real_name',
            field=models.CharField(default=datetime.datetime(2016, 5, 19, 6, 37, 8, 553834, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='weight',
            field=models.PositiveIntegerField(default=0, verbose_name='Weight'),
        ),
        migrations.AlterField(
            model_name='character',
            name='age',
            field=models.PositiveIntegerField(default=0, verbose_name='Born'),
        ),
    ]
