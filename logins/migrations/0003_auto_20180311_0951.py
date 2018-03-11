# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-11 09:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logins', '0002_auto_20180310_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('postText', models.TextField()),
                ('postDate', models.DateTimeField()),
                ('likedCnt', models.IntegerField(default=0)),
                ('dislikedCnt', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'posts',
            },
        ),
        migrations.AddField(
            model_name='userdetails',
            name='registeredDate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='posts',
            name='userDetailsId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logins.userDetails'),
        ),
    ]