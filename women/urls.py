from django.urls import path, re_path
from .views import index, categories, archive, pageNotFound, about

urlpatterns = [
    path('', index, name='index'),
    path('cats/<slug:cat>', categories, name='category'),  # slug = text/int
    path('about/', about, name='about'),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive, name='archive')
    # регулярки [0-9] - разрешенные цифры , {4} - разрешенное кол-во цифр
]

handler404 = pageNotFound  # Обработчик Хэндлеров, дебюг в false
