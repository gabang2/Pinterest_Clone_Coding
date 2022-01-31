from django.contrib import admin
from django.urls import path, include
from accountapp.views import hello_world

app_name='hello_world'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world')
]
