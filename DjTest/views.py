'''
Created on Dec 5, 2017

@author: intesarAlam
'''
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Intesar you did it nicely");
