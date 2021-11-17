from django.urls import path, include
from django.conf.urls import url
from django.views.decorators.cache import cache_page
from .views import AuthorList, AuthorDetail, PostList, PostDetail,PostFind,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,CategorySubscribe, subscribe ,unsubscribe ,mail_test    # импортируем наше представление
from .views import (
    DefaultFormByFieldView,
    DefaultFormsetView,
    DefaultFormView,
    FormHorizontalView,
    FormInlineView,
    FormWithFilesView,
    HomePageView,
    MiscView,
    PaginationView,
)



urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно, почему
    path('authors/', AuthorList.as_view()),
    # т. к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('authors/<int:pk>', AuthorDetail.as_view()),
    # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно, почему
    path('news/', PostList.as_view()),


    # т. к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('news/<int:pk>', PostDetail.as_view()),

    # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    # path('', PostList.as_view()),
    # # т. к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    # path('<int:pk>', PostDetail.as_view()),
    # # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    path('search/', PostFind.as_view()),
    url(r"^$", cache_page(60*5)(PostList.as_view()), name="home"),
    url(r"^formset$", DefaultFormsetView.as_view(), name="formset_default"),
    url(r"^form$", DefaultFormView.as_view(), name="form_default"),
    url(r"^form_by_field$", DefaultFormByFieldView.as_view(), name="form_by_field"),
    url(r"^form_horizontal$", FormHorizontalView.as_view(), name="form_horizontal"),
    url(r"^form_inline$", FormInlineView.as_view(), name="form_inline"),
    url(r"^form_with_files$", FormWithFilesView.as_view(), name="form_with_files"),
    url(r"^pagination$", PaginationView.as_view(), name="pagination"),
    url(r"^misc$", MiscView.as_view(), name="misc"),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),  # Ссылка на детали товара
    path('create/', PostCreateView.as_view(), name='post_create'),  # Ссылка на создание товара
    path('update/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    # path('category/<int:pk>', cache_page(60*5)CategorySubscribe.as_view(), name='post_category'),
    # path('category/<int:pk>', subscribe_category, name='subscribe_category'),
    # path('category/<int:pk>', unsubscribe_category, name='unsubscribe_category'),
    path('subscribe/<int:pk>', subscribe, name='subscribe'),

    path('unsubscribe/<int:pk>', unsubscribe, name='unsubscribe'),
    path('mail_test/', mail_test, name='mail_test'),

]
