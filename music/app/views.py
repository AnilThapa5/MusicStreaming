from django.shortcuts import render

from django.http import HttpResponse
from .models import Blog
# Create your views here.


def index(request):
    return render(request, 'index.html')


class Blogs(object):
    pass


def blog(request):

    blog1 = Blog.objects.all()

    return render(request, "blog.html", {'blog1': blog1})
