from django.urls import path
from .views import ProductsList, ProductDetail  # импортируем наше представление
from django.urls import path, include
urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно, почему
    path('', ProductsList.as_view()),
    # т. к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('<int:pk>', ProductDetail.as_view()),
    # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('pages/', include('django.contrib.flatpages.urls')),
#     path('products/', include('simpleapp.urls')),  # делаем так, чтобы все адреса из нашего приложения (simpleapp/urls.py) сами автоматически подключались когда мы их добавим.
# ]
