from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from blog.models import Article

def home(request):
    articles = Article.objects.all()
    return render(request, 'blog/home.html', {'dernier_articles': articles})

def view_post(request, id_post):
    article = Article.objects.get(id=id_post)
    return render(request, 'blog/post.html', {'post': article})