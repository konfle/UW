from django.shortcuts import render
from .models import PostTraining
from django.utils import timezone


def index(request):
    return render(request, "uwapp/index.html", {})


def about(request):
    return render(request, "uwapp/about.html", {})


def projects(request):
    posts = PostTraining.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, "uwapp/projects.html", {'posts': posts})


def gallery(request):
    return render(request, "uwapp/gallery.html", {})


def contact(request):
    return render(request, "uwapp/contact.html", {})
