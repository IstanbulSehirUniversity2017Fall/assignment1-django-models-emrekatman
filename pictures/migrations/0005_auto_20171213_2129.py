# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-13 18:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0004_auto_20171213_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='painter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pictures.Painter'),
        ),
        migrations.AlterField(
            model_name='pictures',
            name='picture_name',
            field=models.CharField(max_length=150),
        ),
    ]