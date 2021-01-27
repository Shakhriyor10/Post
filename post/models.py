from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    age = models.IntegerField(verbose_name='Возраст')

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Post(models.Model):
    title = models.CharField(verbose_name="название", max_length=150)
    description = models.TextField(verbose_name="описание")
    created = models.DateTimeField(verbose_name="создана", auto_now_add=True)
    bool = models.BooleanField(default=False, verbose_name="Сохранить в черновик")
    image = models.ImageField(verbose_name="изображения", upload_to='post-photo/', null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.CharField(max_length=255, verbose_name='Описание')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
