from django.db.models.signals import post_save
from django.dispatch import receiver # импортируем нужный декоратор
from django.core.mail import mail_managers

from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from .models import Post



@receiver(post_save, sender=Post)
def notify_subscribers(sender, instance, created, **kwargs):
    """ Отправляет по почте информацию, что добавлен новый пост в категории, на которую подписан пользователь """
    if created:
        categories = instance.postCategory.all()
        for category in categories:
            subscribers = category.subscribers.all()
            for subscriber in subscribers:
                if subscriber.email:
                    # Отправка HTML
                    html_content = render_to_string(
                        'email_message.html', {
                            'user': subscriber,
                            'text': f'{instance.text[:50]}',
                            'post': instance.title,
                        }
                    )
                    msg = EmailMultiAlternatives(
                        subject=f'Привет, {subscriber.username}. Новая статья ',
                        from_email='test@shirshakov.ru',
                        to=[subscriber.email],
                    )
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()