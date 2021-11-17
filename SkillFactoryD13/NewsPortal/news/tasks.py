from celery import shared_task
import time

from .models import Post
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
import datetime
from datetime import datetime, timedelta, date
from django.utils.timezone import utc

@shared_task
def hello():
    time.sleep(10)
    print("Hello, world!")


@shared_task
def printer(N):
    for i in range(N):
        time.sleep(1)
        print(i+1)

@shared_task
def week_email_sending():
    #  Your job processing logic here...
    emailsPosts = {}

    users = User.objects.all()
    for user in users:
        emailsPosts.update({user.email: []})

    posts = Post.objects.all()
    for post in posts:
        if ((datetime.utcnow().replace(tzinfo=utc) - post.dateCreation) < timedelta(days=7)):
            categories = post.postCategory.all()
            for category in categories:
                subscribers = category.subscribers.all()
                # print(subscribers)
                for subscriber in subscribers:
                    # print(subscriber.email)
                    # print(emailsPosts[subscriber.email])
                    emailsPosts[subscriber.email].append(post)

    for email in emailsPosts:
        # print(emailsPosts[email])
        html_content = render_to_string(
            'scheduler_email.html',
            {
                'posts': emailsPosts[email],
            }
        )
        msg = EmailMultiAlternatives(
            subject=f'Новые статьи ',
            body=f'Здравствуй, . Новая статья в твоём любимом разделе!',
            from_email='test@shirshakov.ru',
            to=[email],
            # to=['mihail@shirshakov.ru'],

        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()