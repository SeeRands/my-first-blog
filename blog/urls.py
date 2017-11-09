# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 23:29:50 2017

@author: Admin
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]