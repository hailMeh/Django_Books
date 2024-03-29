from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

''' ФУНКЦИОНАЛЬНАЯ ГЛАВНАЯ СТРАНИЦА
def index(request):
    books = Book.objects.all().order_by('-time_create')  # Отображение на главной в обратном порядке
    context = {
        'title': 'index',
        'books': books,
    }
    return render(request, 'women/index.html', context=context)
'''


class IndexView(ListView):
    model = Book
    template_name = 'women/index.html'
    paginate_by = 2  # пагинация в base.html
    context_object_name = 'books'  # Для вывода в шаблон по данному имени,а не object_list
    # extra_context = {'title': 'Главная страница'}  # Статический контент для шаблона
    queryset = Book.objects.all().order_by('-time_create').select_related(
        'category')  # Отображение на главной в обратном порядке. Select_related для оптимизации загрузки из БД

    # def get_queryset(self):
    #   return Women.objects.filter(is_published=True)
    # Queryset = Book.objects.filter(title__icontains='django')[:5]  Получение 5 книг, содержащих слово 'django' в заголовке
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'My Books'
        return context


''' ФУНКЦИОНАЛЬНАЯ СТРАНИЦА КАТЕГОРИЙ
def show_category(request, category_slug):
    book = Book.objects.filter(category__slug=category_slug)
    context = {
        'book': book,
        'title': 'category',
    }
    return render(request, 'women/show_category.html', context=context)
'''


class CategoryView(ListView):
    model = Book
    template_name = 'women/show_category.html'
    context_object_name = 'book'  # обращение к модели через
    allow_empty = False  # Если пусто то на 404
    paginate_by = 2  # пагинация в base.html

    def get_context_data(self, *, object_list=None, **kwargs):  # Шаблонная запись для изменения/отображения, гибко!
        context = super().get_context_data(**kwargs)
        context['title'] = 'Category - ' + str(context['book'][0].category)
        context['category'] = Book.objects.filter(category__slug=self.kwargs['slug']).select_related('category')
        return context

    def get_queryset(self):  # ОРМ можно применять через служебную функцию
        return Book.objects.filter(category__slug=self.kwargs['slug'], is_published=True).select_related('category')


'''
def archive(request, slug):
    if int(slug) > 2022:  # Если год больше нынешнего, дай ошибку,которая перенаправит на хэндлер404
        raise Http404()  # return redirect('/')
    book = Book.objects.filter(year__slug=slug)
    context = {
        'title': 'archive',
        'book': book,
    }
    return render(request, 'women/archives.html', context=context)
'''


class ArchiveView(ListView):
    model = Book
    template_name = 'women/archives.html'
    context_object_name = 'book'
    paginate_by = 2  # пагинация в base.html

    def get_context_data(self, *, object_list=None, **kwargs):  # Шаблонная запись для изменения/отображения, гибко!
        context = super().get_context_data(**kwargs)
        context['title'] = 'Year - ' + str(context['book'][0].year)
        context['book_year'] = Book.objects.filter(year__date=self.kwargs['slug'])
        return context

    def get_queryset(self):  # ОРМ можно применять через служебную функцию
        return Book.objects.filter(year__slug=self.kwargs['slug'], is_published=True)


def about(request):
    context = {
        'title': 'about',
    }
    return render(request, 'women/about.html', context=context)


''' ФУНКЦИОНАЛЬНАЯ ФОРМА ДЛЯ ДОБАВЛЕНИЯ КНИГИ
def addbook(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddBookForm()

    context = {
        'title': 'add_book',
        'form': form
    }
    return render(request, 'women/add_book.html', context=context)
'''


class AddBookView(LoginRequiredMixin, CreateView):
    form_class = AddBookForm
    template_name = 'women/add_book.html'
    login_url = reverse_lazy('index')  # Редирект если пользователь неавторизован, миксин в работе.
    raise_exception = True  # Если пользователь неавторизован, то доступ запрещен

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Adding'
        return context

    success_url = reverse_lazy(
        'index')  # Минует обычный reverse,который при добавлении обьекта направил
    # Бы url на детали добавленного обьекта, Lazy делает reverse только по указанному маршруту
    # И ждёт пока обьект создатся и только потом делает перенаправление, рекомендовано вместо обычно


def contact(request):
    context = {
        'title': 'contact',
    }
    return render(request, 'women/contact.html', context=context)


def pageNotFound(request, exception):  # Страница не найдена
    return render(request, 'women/Error.html', {'title': 'Page not found'})


def authNeed(request, exception):  # Страница не найдена
    return render(request, 'women/403.html', {'title': 'Access denied'})


class BookView(DetailView):
    model = Book
    template_name = 'women/show_book.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['book']
        return context
