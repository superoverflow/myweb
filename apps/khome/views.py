from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
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

def toggle(request, param):
    if param not in state.keys():
        return JsonResponse({"Error":1})

    state[param]  = not(state[param])
    return JsonResponse(state)

def check_state(reqeust):
    return JsonResponse(state)