'''
Created on Dec 5, 2017

@author: intesarAlam
'''
from django.conf.urls import url
from DjTest import views
from django.http.response import HttpResponse
urlpatterns=[
      url(r'^$',views.index,name='index'),
    ]