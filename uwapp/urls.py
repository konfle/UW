from . import views
from django.contrib import admin
from django.urls import path,include
app_name = 'uwapp'
urlpatterns = [
    path('', views.index, name='index'),

    ]
