from django.shortcuts import render
from datetime import datetime
from django.core.paginator import Paginator
from django.views import View
from .models import Post
from .filters import PostFilter
from .forms import PostForm

# Create your views here.
from django.views.generic import ListView, CreateView, DetailView,UpdateView,DeleteView # импортируем необходимые дженерики
from .models import Author, Category, Post, PostCategory, Comment
from django.contrib import messages
from django.core.files.storage import default_storage
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models.fields.files import FieldFile
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from .forms import ContactForm, ContactFormSet, FilesForm
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

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
    form_class = PostForm
    def get_context_data(self, **kwargs):# забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        context['categories'] = Category.objects.all()
        context['authors'] = Author.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        # берём значения для нового товара из POST-запроса отправленного на сервер
        # title = request.POST['title']
        # author_id = request.POST['author']
        # author = Author.objects.get(author_id)
        # categoryType = request.POST['category']
        # content = request.POST['content']
        #
        # post = Post(author=author, categoryType=categoryType, title=title,
        #                   content=content)  # создаём Новый пост и сохраняем его
        # post.save()
        # return super().get(request, *args, **kwargs)
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса
        if form.is_valid(): # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новый товар
            form.save()
            return super().get(request, *args, **kwargs)


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

class FakeField(object):
    storage = default_storage


fieldfile = FieldFile(None, FakeField, "dummy.txt")


class HomePageView(TemplateView):
    template_name = "app/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        messages.info(self.request, "hello http://example.com")
        return context


class DefaultFormsetView(FormView):
    template_name = "app/formset.html"
    form_class = ContactFormSet


class DefaultFormView(FormView):
    template_name = "app/form.html"
    form_class = ContactForm


class DefaultFormByFieldView(FormView):
    template_name = "app/form_by_field.html"
    form_class = ContactForm


class FormHorizontalView(FormView):
    template_name = "app/form_horizontal.html"
    form_class = ContactForm


class FormInlineView(FormView):
    template_name = "app/form_inline.html"
    form_class = ContactForm


class FormWithFilesView(FormView):
    template_name = "app/form_with_files.html"
    form_class = FilesForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["layout"] = self.request.GET.get("layout", "vertical")
        return context

    def get_initial(self):
        return {"file4": fieldfile}


class PaginationView(TemplateView):
    template_name = "app/pagination.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lines = []
        for i in range(200):
            lines.append("Line %s" % (i + 1))
        paginator = Paginator(lines, 10)
        page = self.request.GET.get("page")
        try:
            show_lines = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            show_lines = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            show_lines = paginator.page(paginator.num_pages)
        context["lines"] = show_lines
        return context


class MiscView(TemplateView):
    template_name = "app/misc.html"


# дженерик для получения деталей о Посте
class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    queryset = Post.objects.all()

# дженерик для создания объекта. Надо указать только имя шаблона и класс формы, который мы написали в прошлом юните. Остальное он сделает за вас
class PostCreateView(PermissionRequiredMixin,CreateView):
    template_name = 'post_create.html'
    form_class = PostForm
    permission_required = ('news.add_post',)


# дженерик для редактирования объекта
class PostUpdateView(UpdateView):
    template_name = 'post_create.html'
    form_class = PostForm
    permission_required = ('news.change_post',)

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)



# дженерик для удаления товара
class PostDeleteView(DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'

class ProtectedView(LoginRequiredMixin, TemplateView):
    template_name = 'prodected_page.html'

# views.py
class CategorySubscribe(DetailView):
    model = Category
    template_name = 'post_category.html'
    context_object_name = 'post_category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

@login_required
def subscribe(request, pk):
    # Достаем текущего пользователя
    user = request.user
    # Получаем ссылку из адресной строки и берем pk как id категории
    # id = request.META.get('HTTP_REFERER')[-2]
    # id = pk
    # Получаем текущую категорию
    category = Category.objects.get(id=pk)
    # Создаем связь между пользователем и категорией
    category.subscribers.add(user)
    # category.subscribers(user)
    # category.subscribers
    # category.subscribers
    # Сериалезируем переменные для передачи в селери
    # category = f'{category}'

    email = f'{user.email}'
    # success_url = f'/news/category/{category.join(id)}'
    # вызываем таск для асинхронной отправки письмо
    # send_mail_subscribe.delay(category, email)
    send_mail(
        subject=f'{category.categorya}',
        message=f'Вы {request.user} подписались на обновление категории {category}',
        from_email='test@shirshakov.ru',
        # recipient_list=[email, ],
        recipient_list=['mihail@shirshakov.ru'],
    )
    # return redirect('/news')
    # return redirect(f'{success_url}/')
    # return redirect(request.META.get('HTTP_REFERER'))
    return redirect('/posts')
@login_required
def unsubscribe(request):
    # Достаем текущего пользователя
    user = request.user
    # Получаем ссылку из адресной строки и берем pk как id категории
    id = request.META.get('HTTP_REFERER')[-2]
    # Получаем текущую категорию
    category = Category.objects.get(id=id)
    # Разрываем связь между пользователем и категорией
    category.subscribers.remove(user)
    # Сериалезируем переменные для передачи в селери
    category = f'{category}'
    email = f'{user.email}'
    # success_url = f'/news/category/{category.join(id)}'
    # вызываем таск для асинхронной отправки письмо
    # send_mail_unsubscribe.delay(category, email)
    send_mail(
        subject=f'{category}',
        message=f'Вы {request.user} отписались от обновлений {category}',
        from_email='test@shirshakov.ru',
        # recipient_list=[email, ],
        recipient_list=['mihail@shirshakov.ru'],
    )
    # return redirect('/news')
    # return redirect(f'{success_url}/')
    return redirect(request.META.get('HTTP_REFERER'))

def mail_test(request):

    send_mail(
        subject=f'test',
        message=f'test',
        from_email='test@shirshakov.ru',
        recipient_list=['mihail@shirshakov.ru'],
    )
    return redirect('/posts')
