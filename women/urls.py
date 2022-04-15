from django.urls import path
from .views import IndexView, CategoryView, ArchiveView, pageNotFound, about, AddBookView, contact, BookView, authNeed
from django.views.decorators.cache import cache_page

urlpatterns = [
    # path('', cache_page(60)(IndexView.as_view()), name='index'),
    # Кэш Всей страницы, если нужен кэш частями, то в шаблоне пример
    path('', IndexView.as_view(), name='index'),
    path('category/<slug:slug>/', CategoryView.as_view(), name='category'),
    path('about/', about, name='about'),
    path('archive/<slug:slug>/', ArchiveView.as_view(), name='archive'),
    path('addbook/', AddBookView.as_view(), name='add_book'),
    path('contact/', contact, name='contact'),
    path('book/<slug:slug>/', BookView.as_view(), name='show_book'),
]
