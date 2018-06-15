from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from collections import deque
from .utils import search_youtube,download_youtube, remove_vocal, Result

# Create your views here.
playlist = deque()
state = { 'vocal': False,
          'play': True,
          'skip': True}

def index(request):
    template = loader.get_template("khome/index.html")
    context = { 'playlist': playlist,
                'control_page': request.build_absolute_uri('control') }
    return HttpResponse(template.render(context))

def khome(request, video_id):
    template = loader.get_template("khome/play.html")
    context = { "video_id" : video_id }
    return HttpResponse(template.render(context))

def control(request):
    template = loader.get_template("khome/control.html")
    context = { 'playlist': playlist }
    return HttpResponse(template.render(context))

def search(request, query):
    results = search_youtube(query)
    template = loader.get_template("khome/search_result.html")
    context = {"items" : results}
    return HttpResponse(template.render(context))

def download(request, video_id, video_title):
    download_youtube(settings.MEDIA_ROOT, video_id)
    remove_vocal(f'{settings.MEDIA_ROOT}/{video_id}.mp3', f'{settings.MEDIA_ROOT}/{video_id}-music.mp3')
    playlist.append(Result(video_id, video_title))
    return HttpResponse("Success: " + video_id)

def toggle(request, param):
    if param not in state.keys():
        return JsonResponse({"Error":"no such key [{}]".format(param)})

    state[param]  = not(state[param])
    return JsonResponse(state)

def check_state(reqeust):
    return JsonResponse(state)


def show_playlist(request):
    return JsonResponse({'playlist':list(playlist)})

def pop_playlist(request):
    if len(playlist) > 0:
        playlist.popleft()
    return JsonResponse({'playlist': list(playlist)})
