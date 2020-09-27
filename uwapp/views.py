from django.shortcuts import render


def index(request):
    return render(request, "uwapp/index.html", {})
