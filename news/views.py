from django.shortcuts import render
from django.http import HttpResponse
from .models import News

def index(request):
    news = News.objects.all()
    return render(request, 'news/index.html', {'news': news, 'title': 'List News'})

def test(request):
    return HttpResponse('<h1>Django App</h1>')

