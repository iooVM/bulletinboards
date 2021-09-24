python manage.py flush

py manage.py shell

from news.models import *

u1 = User.objects.create_user(username='User11')
u2 = User.objects.create_user(username='User22')

Author.objects.create(authorUser=u1)

Author.objects.create(authorUser=u2)

Category.objects.create(categorya='PO')

Category.objects.create(categorya='P1')

Category.objects.create(categorya='P2')

Category.objects.create(categorya='P3')

author = Author.objects.get(id=1)

Post.objects.create(author=author, categoryType='NW', title='Ntetle1', content='Ntext1')

Post.objects.create(author=author, categoryType='AR', title='Atetle1', content='Atext1')

Post.objects.create(author=author, categoryType='AR', title='Atetle2', content='Atext2')

author2 = Author.objects.get(id=2)

Post.objects.create(author=author2, categoryType='NW', title='Ntetle1', content='Ntext1')

Post.objects.create(author=author2, categoryType='AR', title='Atetle1', content='Atext1')

Post.objects.create(author=author2, categoryType='AR', title='Atetle2', content='Atext2')

Post.objects.get(id=1)

Post.objects.all()

Post.objects.get(id=1).postCategory.add(Category.objects.get(id=1))

Post.objects.get(id=1).postCategory.add(Category.objects.get(id=2))

Post.objects.get(id=2).postCategory.add(Category.objects.get(id=3))

Post.objects.get(id=3).postCategory.add(Category.objects.get(id=4))

Post.objects.get(id=1).postCategory.all()

Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).authorUser,
                       content='comment1')

Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).authorUser,
                       content='comment2')

Comment.objects.create(commentPost=Post.objects.get(id=2), commentUser=Author.objects.get(id=2).authorUser,
                       content='comment3')

Comment.objects.create(commentPost=Post.objects.get(id=3), commentUser=Author.objects.get(id=2).authorUser,
                       content='comment4')

Comment.objects.get(id=1).like()

Comment.objects.get(id=1).rating

Comment.objects.get(id=1).dislike()

Comment.objects.get(id=1).like()

Comment.objects.get(id=1).rating

Comment.objects.get(id=1).like()
Comment.objects.get(id=1).like()
Comment.objects.get(id=1).like()

Comment.objects.get(id=2).dislike()
Comment.objects.get(id=2).dislike()
Comment.objects.get(id=2).dislike()

Comment.objects.get(id=3).like()

Comment.objects.get(id=3).like()

Comment.objects.get(id=3).like()

Comment.objects.get(id=4).dislike()

a1 = Author.objects.get(id=1)

a2 = Author.objects.get(id=2)

a1.ratingAuthor

a2.ratingAuthor

a1.update_rating()
a2.update_rating()

a1.ratingAuthor

a2.ratingAuthor

Post.objects.get(id=1).rating

Post.objects.get(id=1).like()
Post.objects.get(id=1).like()

a1.ratingAuthor

aa = Author.objects.order_by('-ratingAuthor')

aa[0].ratingAuthor

aa[0].authorUser.username

bestPost = Post.objects.order_by('-rating')

bestPost[0]

str(bestPost[0].rating) + ',  ' + str(bestPost[0].author.authorUser) + ',  ' + str(bestPost[0].title) + ',  ' + str(
    bestPost[0].preview()) + ',  ' + str(bestPost[0].dateCreation)

Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).authorUser,
                       content='comment12')
Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).authorUser,
                       content='comment13')
Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).authorUser,
                       content='comment14')

C = Comment.objects.filter(commentPost=bestPost[0])

C.values('dateCreation', 'commentUser', 'rating', 'content')
