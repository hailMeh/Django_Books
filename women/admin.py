from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Book, Category, Year

# Register your models here.
admin.site.site_title = 'my_books'
admin.site.site_header = 'Administrate this!'


class BookAdmin(admin.ModelAdmin):
    save_on_top = True
    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")
        else:
            return 'No img'

    list_display = ('id', 'title', 'time_create', 'get_html_photo', 'is_published') # Что отображать
    list_display_links = ('id', 'title')  # Линкс на поля для перехода
    fields = ('title', 'slug', 'category', 'content', 'photo', 'is_published')
    search_fields = ('title', 'content') # поиск по полям
    list_editable = ('is_published',) # что можно редактировать
    list_filter = ('is_published', 'time_create')  # фильтрация по
    prepopulated_fields = {"slug": ("title",)}  # Автоматические преобразование из field в slug



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class YearAdmin(admin.ModelAdmin):
    list_display = ('id', 'date')
    list_display_links = ('id', 'date')
    search_fields = ('date',)
    prepopulated_fields = {"slug": ("date",)}


admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Year, YearAdmin)

