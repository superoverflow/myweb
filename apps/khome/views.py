from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from collections import deque

# Create your views here.
playlist = deque()
state = { 'vocal': False,
          'play': True,
          'skip': True}

def control(request):
    template = loader.get_template("khome/control.html")
    context = { 'playlist': playlist }
    return HttpResponse(template.render(context))

def search(request, query):
    return HttpResponse()
