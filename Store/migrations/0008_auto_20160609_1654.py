# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-09 23:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0007_auto_20160609_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(default=1, verbose_name='date of transaction'),
        ),
    ]
