# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-12 19:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
