from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-input'}))  # Добавить в регистрацию новое поле

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
