from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.

def index(request):
    blog_title = "insta posts"
    posts = [
        {'title': 'post 1' , 'content': 'content of post 1'},
        {'title': 'post 2' , 'content': 'content of post 2'},
        {'title': 'post 3' , 'content': 'content of post 3'},
        {'title': 'post 4' , 'content': 'content of post 4'},
    ]
    return render(request,'blog/index.html', {'blog_title': blog_title, 'posts': posts})

def detail(request, post_id):
    return render(request,'blog/detail.html')

def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url)'))

def new_url_view(request):
    return HttpResponse("This is the new url")