from django import template
from women.models import *

# Пользовательские таги для принципа DRY

register = template.Library()


@register.simple_tag()  # Загружай категории книг, используй данный тэг в base.html и можно использовать в любом шаблоне
def get_categories():
    return Category.objects.all()


@register.simple_tag()
def get_year():
    return Year.objects.all().order_by('-date')
