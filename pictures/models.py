# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Painter(models.Model):
    name_surname = models.CharField(max_length=100)
    def __str__(self):
        return self.name_surname

class Pictures(models.Model):
    painter = models.ForeignKey(Painter, on_delete=models.CASCADE)
    picture_name = models.CharField(max_length=150)
    location = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    date = models.DateTimeField()
    def __str__(self):
        return self.picture_name



