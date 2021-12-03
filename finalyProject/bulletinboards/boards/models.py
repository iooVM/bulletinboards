from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# Модель автора объявлений
class Author(models.Model):
    # связь «один к одному» с встроенной моделью пользователей User
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    # рейтинг пользователя.
    ratingAuthor = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.authorUser}'


# Модель категории
class Category(models.Model):
    # Имя категории
    categorya = models.CharField(
        max_length=32,
        unique=True,
    )

    # subscribers = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # Связь многим ко многим для оповещения подписчиков категорий
    subscribers = models.ManyToManyField(User)

    def __str__(self):
        return f'{self.categorya}'


# Модель Объявления
class Announce(models.Model):
    # Связь одн к многим для Автора
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # Связь с Объявлениякатегориями
    AnnounceCategory = models.ManyToManyField(Category, through='AnnounceCategory')
    # Заголовок Объявления
    title = models.CharField(max_length=64, default='Заголовок нового объявления')
    # Текст объявления
    # TODO добавить +картинки+ видеоWYSIWYG
    content = models.TextField(default='Текст нового объявления')

    # Дата создания
    dateCreation = models.DateTimeField(auto_now=True)

    # Предпросмотр Объявления
    def preview(self):
        return self.content[:123] + '...'

    def get_absolute_url(
            self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с объявлениями
        return f'http://127.0.0.1:8000/announce/{self.id}'

    def __str__(self):
        return f'{self.title}'

# Модель ОбъявленияКатегории
class AnnounceCategory(models.Model):
    #Связи c моделями  Объявления Категории
    AnnounceThrough = models.ForeignKey(Announce, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.categoryThrough}'



# Модель комментарии
class Comment(models.Model):
    commentPost = models.ForeignKey(Announce, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(default='Текст комментария ')
    dateCreation = models.DateTimeField(auto_now_add=True)

