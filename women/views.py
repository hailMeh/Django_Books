from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import Book, Category


def index(request):
    books = Book.objects.all()
    cats = Category.objects.all()
    context = {
        'title': 'index',
        'books': books,
        'cats': cats
    }
    return render(request, 'women/index.html', context=context)


def show_category(request, category):
    book = Book.objects.filter(category_id=category)
    cats = Category.objects.all()
    context = {
        'book': book,
        'cats': cats,
        'title': {category},
    }
    return render(request, 'women/show_category.html', context=context)


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
