from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import Book, Category, Year


def index(request):
    books = Book.objects.all()
    cats = Category.objects.all()
    year = Year.objects.all()
    context = {
        'title': 'index',
        'books': books,
        'cats': cats,
        'year': year
    }
    return render(request, 'women/index.html', context=context)


def show_category(request, category):
    book = Book.objects.filter(category_id=category)
    cats = Category.objects.all()
    year = Year.objects.all()
    context = {
        'book': book,
        'cats': cats,
        'title': {category},
        'year': year
    }
    return render(request, 'women/show_category.html', context=context)


def archive(request, year):
    if int(year) > 2022:  # Если год больше нынешнего, дай ошибку,которая перенаправит на хэндлер404
        raise Http404()  #  return redirect('/')
    date = Year.objects.all()
    book = Book.objects.filter(year_id=year)
    cats = Category.objects.all()
    context = {
        'title': 'archive',
        'year': date,
        'book': book,
        'cats': cats
    }
    return render(request, 'women/archives.html', context=context)


def about(request):
    cats = Category.objects.all()
    year = Year.objects.all()
    context = {
        'title': 'about',
        'year': year,
        'cats': cats
    }
    return render(request, 'women/about.html', context=context)


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    cats = Category.objects.all()
    year = Year.objects.all()
    context = {
        'title': 'contact',
        'year': year,
        'cats': cats
    }
    return render(request, 'women/contact.html', context=context)


def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):  # Страница не найдена
    return HttpResponseNotFound('NOT FOUND PAGE')


def show_book(request, pk):
    book = Book.objects.get(pk=pk)
    cats = Category.objects.all()
    year = Year.objects.all()
    context = {
        'title': 'show_book',
        'book': book,
        'year': year,
        'cats': cats
    }
    return render(request, 'women/show_book.html', context=context)
