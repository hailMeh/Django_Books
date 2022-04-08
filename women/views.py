from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404


def index(request):
    return render(request, 'women/index.html')


def categories(request, cat):
    '''   if int(cat) > 2020:
       return redirect('index')  # Проверяемый параметр должен совпадать с параметром у URL !!!  '''
    return HttpResponse(f"<h1>Статьи по категориям</h1>{cat}</p>")


def archive(request, year):
    if int(year) > 2022:  # Если год больше нынешнего, дай ошибку,которая перенаправит на хэндлер404
        raise Http404()  #  return redirect('/')
    return HttpResponse(f'ARCHIVE FOR {year} year')



def pageNotFound(request, exception):  # Страница не найдена
    return HttpResponseNotFound('NOT FOUND PAGE')

