from django.shortcuts import render
from django.views import generic
from.models import Post


def PostList(request):

    template = 'blog/blog.html'
    return render(request, template)
