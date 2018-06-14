from django.urls import path

from . import views

urlpatterns = [
    path('control', views.control, name='control'),
    path('search/<query>', views.search, name='search'),
    path('toggle/<param>', views.toggle, name='toggle'),
    path('state', views.check_state, name='state')
]