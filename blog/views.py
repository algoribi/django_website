from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request) :
    Posts = Post.objects.all()
    return render(
        request,
        'blog/index.html',
        {
            'posts' : Posts,
        }
    )