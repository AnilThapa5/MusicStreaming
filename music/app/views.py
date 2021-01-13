from django.shortcuts import render

from django.http import HttpResponse
from .models import Blog, Song


# Create your views here.


def index(request):
    song1 = Song.objects.all()
    return render(request, "index.html", {'song1': song1})


def blog(request):
    blog1 = Blog.objects.all()
    return render(request, "blog.html", {'blog1': blog1})




