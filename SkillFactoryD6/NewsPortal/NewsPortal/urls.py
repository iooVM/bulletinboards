"""NewsPortal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    # path('authors/', include('news.urls')),
    path('posts/', include('news.urls')),
    path('authors/<int:pk>', include('news.urls')),
    path('news/<int:pk>', include('news.urls')),
    path('search/', include('news.urls')),
    path('authors/', include('news.urls')),
    path('<int:pk>/', include('news.urls')),  # Ссылка на детали товара
    path('create/', include('news.urls')),  # Ссылка на создание товара
    # path('update/<int:pk>', include('news.urls')),
    # path('delete/<int:pk>', include('news.urls')),
    # path('category/<int:pk>', include('news.urls')),
    # path('category/<int:pk>', include('news.urls')),
    # path('category/<int:pk>', include('news.urls')),

    path('', include('protect.urls')),
    #    path('', include('news.urls')),

    path('sign/', include('sign.urls')),
    path('accounts/', include('allauth.urls')),
    # path('mail_test/', include('news.urls')),

    # делаем так, чтобы все адреса из нашего приложения (simpleapp/urls.py) сами автоматически подключались когда мы их добавим.
]
