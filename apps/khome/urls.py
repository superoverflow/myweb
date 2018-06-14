from django.urls import path

from . import views

urlpatterns = [
    path('control', views.control, name='control'),
    path('search/<query>', views.search, name='search')
]