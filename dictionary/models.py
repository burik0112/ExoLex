from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Term(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    name_uz = models.CharField(max_length=200, blank=True, null=True)
    name_ru = models.CharField(max_length=200, blank=True, null=True)
    name_en = models.CharField(max_length=200, blank=True, null=True)

    description_uz = models.TextField(default='', blank=True, null=True)
    description_ru = models.TextField(default='', blank=True, null=True)
    description_ru = models.TextField(default='', blank=True, null=True)
    description_en = models.TextField(default='', blank=True, null=True)
    example = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_uz


class Article(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title