# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-11 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logins', '0004_auto_20180311_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='id',
            field=models.AutoField(max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='id',
            field=models.AutoField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
