from django.http import HttpResponse
from django.shortcuts import render,redirect

from .models import *


menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

def index(request):
    posts = Mobile.objects.all()
    return render(request, 'mobilephone/index.html', {'posts': posts,'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'mobilephone/about.html', {'menu': menu, 'title': 'О сайте'})

def categories(request,catid):
    if request.POST:
        print(request.POST)

def categories(request, catid):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}<p/>")

def archive(request, year):
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")