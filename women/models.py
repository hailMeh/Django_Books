from django.db import models
from django.urls import reverse

#  https://djbook.ru/rel3.0/ref/models/fields.html - ВСЕ ДОСТУПНЫЕ ПОЛЯ В МОДЕЛЯХ


class Book(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)  # Бланк можно оставить незаполненным,ругаться не будет
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)  # pip install pillow
    time_create = models.DateTimeField(
        auto_now_add=True) # Позволяет фиксировать текущее время только в момент первого добавления записи в таблицу БД;
    time_update = models.DateTimeField(
        auto_now=True)  # Фиксирует текущее время всякий раз при изменении или добавлении записи в таблицу БД
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)  # Null чтобы не ругалось
    year = models.ForeignKey('Year', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_book', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Книги'
        verbose_name_plural = 'Книги'


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category': self.pk})

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'


class Year(models.Model):
    date = models.CharField(max_length=100, verbose_name='Издана в')

    def __str__(self):
        return self.date

    def get_absolute_url(self):
        return reverse('archive', kwargs={'year': self.pk})

    class Meta:
        verbose_name = 'Год издания'
        verbose_name_plural = 'Год издания'
