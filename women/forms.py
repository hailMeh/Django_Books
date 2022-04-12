from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'slug', 'photo', 'content', 'year', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 10, 'rows': 2}),
        }

    def clean_title(self):   #  Пользовательские ограничения в форме
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')
        return title