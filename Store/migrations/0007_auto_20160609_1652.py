# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-09 23:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0006_auto_20160609_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineitem',
            name='quantity',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='zip',
            field=models.IntegerField(default=-1),
        ),
    ]
