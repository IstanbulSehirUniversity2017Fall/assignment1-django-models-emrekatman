from django.conf.urls import url
from django.contrib import admin
from .views import index_entry

urlpatterns = [

    url(r'^(?P<id>\d+)/$',index_entry),
]