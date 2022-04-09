from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import Book


def index(request):
    books = Book.objects.all()
    return render(request, 'women/index.html', {'title': 'index', 'books': books})


def categories(request, cat):
    '''   if int(cat) > 2020:
       return redirect('index')  # Проверяемый параметр должен совпадать с параметром у URL !!!  '''
    return HttpResponse(f"<h1>Статьи по категориям</h1>{cat}</p>")


def archive(request, year):
    if int(year) > 2022:  # Если год больше нынешнего, дай ошибку,которая перенаправит на хэндлер404
        raise Http404()  #  return redirect('/')
    return render(request, 'women/archives.html', {'title': 'archives'})


def about(request):
    return render(request, 'women/about.html', {'title': 'about'})


def pageNotFound(request, exception):  # Страница не найдена
    return HttpResponseNotFound('NOT FOUND PAGE')

