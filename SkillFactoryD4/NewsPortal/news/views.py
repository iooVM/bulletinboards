from django.shortcuts import render
from datetime import datetime
from django.core.paginator import Paginator
from django.views import View
from .models import Post
from .filters import PostFilter

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
#    queryset = Post.objects.order_by('-dateCreation') # Сортировка по дате создания, rjcnfkmysq cgjcj,
    ordering = ['dateCreation']
    paginate_by = 10
    # def get_context_data(self, **kwargs):# забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
    #     context = super().get_context_data(**kwargs)
    #     context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
    #     return context

# создаём представление, в котором будут детали конкретного отдельного товара
class PostDetail(DetailView):
    model = Post  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'post.html'  # название шаблона будет product.html
    context_object_name = 'post'  # название объекта. в нём будет

class PostFind(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'posts'
    ordering = ['dateCreation']
    paginate_by = 3

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, **kwargs):# забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context

class PostSimple(View):

    def get(self, request):
        posts = Post.objects.order_by('-price')
        p = Paginator(posts,
                      1)  # создаём объект класса пагинатор, передаём ему список наших товаров и их количество для одной страницы

        posts = p.get_page(request.GET.get('page',
                                              1))  # берём номер страницы из get-запроса. Если ничего не передали, будем показывать первую страницу.
        # теперь вместо всех объектах в списке товаров хранится только нужная нам страница с товарами

        data = {
            'posts': posts,
        }
        return render(request, 'product_list.html', data)

