# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-13 18:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0002_painter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='painter',
            name='picture',
        ),
        migrations.AddField(
            model_name='pictures',
            name='picture',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pictures.painter'),
        ),
    ]
