from django.urls import path
from .views import index, category

urlpatterns = [
    path('', index, name='index'),
    path('cats/', category, name='category'),
]
