from . import views
from django.contrib import admin
from django.urls import path, include

app_name = 'uwapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('o-nas/', views.about, name='about'),
    path('projekty/', views.projects, name='projects'),
    path('galeria/', views.gallery, name='gallery'),
    path('kontakt/', views.contact, name='contact'),
    ]
