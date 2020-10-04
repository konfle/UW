from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse

from .models import PostTraining
from .forms import ContactForm


def index(request):
    return render(request, "uwapp/index.html", {})


def about(request):
    return render(request, "uwapp/about.html", {})


def projects(request):
    posts = PostTraining.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, "uwapp/projects.html", {'posts': posts})


def gallery(request):
    return render(request, "uwapp/gallery.html", {})

'''
def contact(request):
    return render(request, "uwapp/contact.html", {})
'''

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return render(request, 'uwapp/index.html', {})
    else:
        form = ContactForm()
    return render(request, 'uwapp/contact.html', {'form': form})
