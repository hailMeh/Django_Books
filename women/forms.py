from django import forms
from django.core.exceptions import ValidationError
from .models import *
from captcha.fields import CaptchaField


class AddBookForm(forms.ModelForm):
    captcha = CaptchaField()  #  https://django-simple-captcha.readthedocs.io/en/latest/advanced.html
    class Meta:
        model = Book
        fields = ['title', 'slug', 'photo', 'content', 'year', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 0, 'rows': 2}),
        }

    def clean_title(self):   #  Пользовательские ограничения в форме
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Length is more than 200 keywords')
        return title
