from django.contrib import admin

from dictionary.models import Category, Term, Article

# Register your models here.

admin.site.register(Category)
admin.site.register(Term)
admin.site.register(Article)
