from django.urls import path, re_path
from .views import IndexView, CategoryView, archive, pageNotFound, about, AddBookView, contact, login, BookView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('category/<slug:slug>/', CategoryView.as_view(), name='category'),
    path('about/', about, name='about'),
    path('archive/<slug:slug>/', archive, name='archive'),
    path('addbook/', AddBookView.as_view(), name='add_book'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('book/<slug:slug>/', BookView.as_view(), name='show_book'),
]

handler404 = pageNotFound  # Обработчик Хэндлеров, дебюг в false
