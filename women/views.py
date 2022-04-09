from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import Book


def index(request):
    books = Book.objects.all()
    context = {
        'title': 'index',
        'books': books
    }
    return render(request, 'women/index.html', context=context)


def categories(request, cat):
    '''   if int(cat) > 2020:
       return redirect('index')  # Проверяемый параметр должен совпадать с параметром у URL !!!  '''
    return HttpResponse(f"<h1>Статьи по категориям</h1>{cat}</p>")


def archive(request, year):
    if int(year) > 2022:  # Если год больше нынешнего, дай ошибку,которая перенаправит на хэндлер404
        raise Http404()  #  return redirect('/')
    context = {
        'title': 'archive'
    }
    return render(request, 'women/archives.html', context=context)


def about(request):
    context = {
        'title': 'about'
    }
    return render(request, 'women/about.html', context=context)


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    context = {
        'title': 'contact'
    }
    return render(request, 'women/contact.html', context=context)


def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):  # Страница не найдена
    return HttpResponseNotFound('NOT FOUND PAGE')


def show_book(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        'title': 'show_book',
        'book': book
    }
    return render(request, 'women/show_book.html', context=context)
