from django.urls import path

from customer.forms import LoginForm
from customer.views import register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', register, name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html',
        authentication_form=LoginForm
    ), name='login'),
]
