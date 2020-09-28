from django.shortcuts import render
from .models import PostTraining
from django.utils import timezone


def index(request):
    posts = PostTraining.objects.filter(data_opublikowania__lte=timezone.now()).order_by('data_opublikowania')
    return render(request, "uwapp/index.html", {'posts': posts})


