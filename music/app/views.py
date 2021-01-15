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


def search(request):
    query = request.GET['query']
    if len(query) > 78:
        song1 = Song.objects.none()
    else:
        songtitle = Song.objects.filter(title__icontains=query)
        songgenres = Song.objects.filter(genres__icontains=query)
        songcatogory = Song.objects.filter(songs__icontains=query)
        songartist = Song.objects.filter(artist__icontains=query)
        song1 = songtitle.union(songgenres).union(songcatogory).union(songartist)

    if song1.count() == 0:
        message.error(request, "No search result found")
    params = {'song1': song1, 'query': query}
    return render(request, 'search.html', params)



