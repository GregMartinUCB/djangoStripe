# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-09 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0004_auto_20160608_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='suitdetail',
            name='crotch',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='suitdetail',
            name='hip',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='suitdetail',
            name='bicep',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='suitdetail',
            name='chest',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='suitdetail',
            name='color',
            field=models.CharField(default=-1, max_length=25),
        ),
        migrations.AlterField(
            model_name='suitdetail',
            name='fit',
            field=models.CharField(default=-1, max_length=25),
        ),
        migrations.AlterField(
            model_name='suitdetail',
            name='front_length',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='suitdetail',
            name='inseam',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='suitdetail',
            name='lapel',
            field=models.CharField(default=-1, max_length=25),
        ),
        migrations.AlterField(
            model_name='suitdetail',
            name='material',
            field=models.CharField(default=-1, max_length=25),
        ),
        migrations.AlterField(
            model_name='suitdetail',
            name='outseam',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='suitdetail',
            name='seat',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='suitdetail',
            name='shoulder',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='suitdetail',
            name='sleeve',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='suitdetail',
            name='thigh',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='suitdetail',
            name='waist',
            field=models.IntegerField(default=-1),
        ),
    ]
