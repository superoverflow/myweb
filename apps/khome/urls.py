from django.urls import path

from . import views

urlpatterns = [

    path('state', views.check_state, name='state'),
    path('toggle/<param>', views.toggle, name='toggle'),
    path('playlist', views.show_playlist, name='playlist'),
    path('popPlaylist', views.pop_playlist, name='pop'),

    path('control', views.control, name='control'),
    path('search/<query>', views.search, name='search'),

]