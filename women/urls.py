from django.urls import path, re_path
from .views import index, show_category, archive, pageNotFound, about, addpage, contact, login, show_book

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category>/', show_category, name='category'),
    # path('cats/<slug:cat>', categories, name='category'),  # slug = text/int
    path('about/', about, name='about'),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive, name='archive'),
    # регулярки [0-9] - разрешенные цифры , {4} - разрешенное кол-во цифр
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('book/<int:pk>/', show_book, name='show_book'),
]

handler404 = pageNotFound  # Обработчик Хэндлеров, дебюг в false
