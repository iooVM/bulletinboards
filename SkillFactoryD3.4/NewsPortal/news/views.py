from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView  # импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from .models import Author, Category, Post, PostCategory, Comment


class AuthorList(ListView):
    model = Author  # указываем модель, объекты которой мы будем выводить
    template_name = 'authors.html'  # указываем имя шаблона, в котором будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'authors'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон

# создаём представление, в котором будут детали конкретного отдельного товара
class AuthorDetail(DetailView):
    model = Author  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'author.html'  # название шаблона будет product.html
    context_object_name = 'author'  # название объекта. в нём будет

class PostList(ListView):
    model = Post # указываем модель, объекты которой мы будем выводить
    # model.order_by('-dateCreation')
    template_name = 'posts.html'  # указываем имя шаблона, в котором будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'posts'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    queryset = Post.objects.order_by('-dateCreation') # Сортировка по дате создания

# создаём представление, в котором будут детали конкретного отдельного товара
class PostDetail(DetailView):
    model = Post  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'post.html'  # название шаблона будет product.html
    context_object_name = 'post'  # название объекта. в нём будет