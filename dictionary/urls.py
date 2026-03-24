from django.urls import path

from dictionary.views import terms, home, term_detail

app_name = 'dictionary'

urlpatterns = [
    path('', home, name='home'),
    path('terms/', terms, name='terms'),
    path('terms/<int:pk>/', term_detail, name='term_detail'),
]
