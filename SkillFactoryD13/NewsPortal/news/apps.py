from django.apps import AppConfig
import redis


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'

    # нам надо переопределить метод ready, чтобы при готовности нашего приложения импортировался модуль со всеми функциями обработчиками
    def ready(self):
        import news.signals

red = redis.Redis(

    host='redis-14105.c250.eu-central-1-1.ec2.cloud.redislabs.com',
    port='14105',
    password='C3GzUeCTXn3AHwlzkR7zWvF3288vkz8w'


)