from django.db.models.signals import post_save
from django.dispatch import receiver # импортируем нужный декоратор
from django.core.mail import mail_managers

from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed

from .models import Post


# в декоратор передаётся первым аргументом сигнал, на который будет реагировать эта функция, и в отправители надо передать также модель
@receiver(post_save, sender=Post)
def notify_subscribers(sender, instance, created, **kwargs):
    """ Отправляет по почте информацию, что добавлен новый пост в категории, на которую подписан пользователь """
#    if created:
#     categories = instance.postCategory.all()
#     for category in categories:
#         subscribers = category.subscribers.all()
#         for subscriber in subscribers:
#             if subscriber.email:
#                 # Отправка HTML
#                 html_content = render_to_string(
#                     'email_message.html', {
#                         'user': subscriber,
#                         'text': f'{instance.text[:50]}',
#                         'post': instance.title,
#                     }
#                 )
#                 msg = EmailMultiAlternatives(
#                     subject=f'Привет, {subscriber.username}. Новая статья ',
#                     from_email='test@shirshakov.ru',
#                     # to=[subscriber.email],
#                     to=['mihail@shirshakov.ru'],
#                 )
#                 msg.attach_alternative(html_content, "text/html")
#                 msg.send()
    #     categories = instance.postCategory.all()
    #     for category in categories:
    #         subscribers = category.subscribers.all()
    #         for subscriber in subscribers:
    #             if subscriber.email:
    emails = []

    categories = instance.postCategory.all()
    for category in categories:
        subscribers = category.subscribers.all()
        for subscriber in subscribers:
            emails.append(subscriber.email)

    html_content = render_to_string(
        'cat_email_message.html',
        {
            'post': instance,
        }
    )
    msg = EmailMultiAlternatives(
        subject=f'{instance.title}, {emails}',
        body=f'Здравствуй, . Новая статья в твоём любимом разделе!',
        from_email='test@shirshakov.ru',
        to=[emails, 'mihail@shirshakov.ru'],
        # to=['mihail@shirshakov.ru'],

    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()

@receiver(m2m_changed, sender=Post.postCategory.through)
def notify_user(sender, action, **kwargs):
    if action == 'post_add':
        instance = kwargs['instance']
        category_id = kwargs['pk_set']
        title = instance.title
        message = instance.text

        html_content = render_to_string(
            'cat_email_message.html',
            {
                'post': instance,
            }
        )
        msg = EmailMultiAlternatives(
    #        subject=f'{instance.title}, {emails}',
            subject=f'{instance.title}',
            body=f'Здравствуй, . Новая статья в твоём любимом разделе!',
            from_email='test@shirshakov.ru',
            to=[emails, 'mihail@shirshakov.ru'],
            # to=['mihail@shirshakov.ru'],

        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()