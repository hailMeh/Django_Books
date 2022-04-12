from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import Book


def index(request):
    books = Book.objects.all()
    context = {
        'title': 'index',
        'books': books,
    }
    return render(request, 'women/index.html', context=context)


def show_category(request, category_slug):
    book = Book.objects.filter(category__slug=category_slug)
    context = {
        'book': book,
        'title': 'category',
    }
    return render(request, 'women/show_category.html', context=context)


def archive(request, year_slug):
    if int(year_slug) > 2022:  # Если год больше нынешнего, дай ошибку,которая перенаправит на хэндлер404
        raise Http404()  #  return redirect('/')
    book = Book.objects.filter(year__slug=year_slug)
    context = {
        'title': 'archive',
        'book': book,
    }
    return render(request, 'women/archives.html', context=context)


def about(request):
    context = {
        'title': 'about',
    }
    return render(request, 'women/about.html', context=context)


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    context = {
        'title': 'contact',
    }
    return render(request, 'women/contact.html', context=context)


def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):  # Страница не найдена
    return HttpResponseNotFound('NOT FOUND PAGE')


def show_book(request, book_slug):
    book = get_object_or_404(Book, slug=book_slug)
    context = {
        'title': book.title,
        'book': book,
    }
    return render(request, 'women/show_book.html', context=context)
