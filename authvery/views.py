from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterUserForm


class RegisterView(CreateView):
    form_class = RegisterUserForm
    template_name = 'authvery/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):  #  Авторизация сразу после регистрации
        user = form.save()
        login(self.request, user)
        return redirect('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Register'
        return context


class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'authvery/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        return context


def user_logout(request): #  Логаут с реквестом
    logout(request)
    return redirect('index')
