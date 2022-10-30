from django.shortcuts import render
from .models import Post

# Create your views here.
# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'posts/posts.html', context)
