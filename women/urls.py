from django.urls import path, re_path
from .views import index, show_category, archive, pageNotFound, about, addbook, contact, login, show_book

urlpatterns = [
    path('', index, name='index'),
    path('category/<slug:category_slug>/', show_category, name='category'),
    path('about/', about, name='about'),
    path('archive/<slug:year_slug>/', archive, name='archive'),
    path('addbook/', addbook, name='add_book'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('book/<slug:book_slug>/', show_book, name='show_book'),
]

handler404 = pageNotFound  # Обработчик Хэндлеров, дебюг в false
