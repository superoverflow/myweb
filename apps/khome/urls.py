from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('play/<video_id>', views.khome, name='play'),

    path('control', views.control, name='control'),
    path('search/<query>', views.search, name='search'),
    path('download/<video_id>/<video_title>', views.download, name='download'),

    path('state', views.check_state, name='state'),
    path('toggle/<param>', views.toggle, name='toggle'),
    path('playlist', views.show_playlist, name='playlist'),
    path('pending', views.show_pending, name='pending'),
    path('popPlaylist', views.pop_playlist, name='pop'),
]