from django.urls import path
from .views import RegisterView, UserLoginView, user_logout

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout')
]
