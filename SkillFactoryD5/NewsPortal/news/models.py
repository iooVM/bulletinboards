from django.db import models
# импортируем для связи «один к одному» с встроенной моделью пользователей User
from django.contrib.auth.models import User
from django.db.models import Sum


# Create your models here.

# Категории Категории новостей/статей


# Модель Автор
class Author(models.Model):
    # cвязь «один к одному» с встроенной моделью пользователей User
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    # рейтинг пользователя.
    ratingAuthor = models.IntegerField(default=0)

    def update_rating(self):
        postRat = self.post_set.aggregate(postRating=Sum('rating'))
        pRat = 0
        pRat += postRat.get('postRating')

        commentRate = self.authorUser.comment_set.aggregate(commentRating=Sum('rating'))
        cRat = 0
        cRat += commentRate.get('commentRating')

        self.ratingAuthor = pRat * 3 + cRat
        self.save()
        pass

    pass
    def __str__(self):
        return f'{self.authorUser}'



'''
Модель Категории 
Максимальная длина 20
Только из Списока кортежей категорий CATEGORYS
По умочанию образование
'''


class Category(models.Model):
    # SPORT = 'SP'
    # SHIT = 'PO'
    # SCHOOLING = 'SH'
    # OTHER = 'OT'
    #
    # # Список кортежей категорий
    # CATEGORYS = [
    #     (SPORT, 'спорт'),
    #     (SHIT, 'политика'),
    #     (SCHOOLING, 'образование'),
    #     (OTHER, 'другое'),

    #    ]
    categorya = models.CharField(
        max_length=32,
        unique=True,
    )

    pass


'''
Модель Статей  или новостей
'''


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья'),
    )
    categoryType = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE)
    #    choices_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #    created_datetime = models.DateTimeField(auto_now_add=True)
    #    modify_datetime = models.DateTimeField(auto_now=True)
    dateCreation = models.DateTimeField(auto_now=True)
#     dateCreation = models.DateField(auto_now=True)
#    dateCreations = models.CharField(max_length=64, default=dateCreation)
    postCategory = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=64, default='Заголовок Ы')
    content = models.TextField(default='Тут текст статьи Ы')
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.content[:123] + '...'

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/news/{self.id}'


# Промежуточная модель для связи «многие ко многим»
class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)
    pass


# Модель комментарии
class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(default='Тут текст комментария')
    dateCreation = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    pass


if __name__ == '__main__':
    print('PyCharm')
