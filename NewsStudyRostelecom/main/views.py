from django.shortcuts import render
from .models import News
from django.http import HttpResponse


def index(request):
    value = -10
    n1 = News('Новость1', 'Text1', '12.12.2023')
    n2 = News('Новость2', 'Text2', '13.12.2023')
    l = [n1,n2]
    context = {'title': 'Страница главная',
               'header1': 'Заголовок страницы',
               # value: value,
               'numbers': l}
    return render(request, "main/index.html", context)


def contacts(request):
    return render(request, "main/contacts.html")


def about(request):
    return render(request, "main/about.html")

def sidebar(request):
    return render(request, "main/sidebar.html")
# Create your views here.
