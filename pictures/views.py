# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse,get_object_or_404
from .models import Painter

# Create your views here.
def index_entry(request,id):
    picture = get_object_or_404(Painter,id=id)
    return HttpResponse(picture)