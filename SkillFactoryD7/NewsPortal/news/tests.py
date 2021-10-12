emailsPosts = {} 

users = User.objects.all()
for user in users:
    emailsPosts.update({user.email : []})

posts = Post.objects.all()
for post in posts:
    categories = post.postCategory.all()
    for category in categories:
        subscribers = category.subscribers.all()
        print(subscribers)
        for subscriber in subscribers:
            print(subscriber.email)
            print(emailsPosts[subscriber.email])
            emailsPosts[subscriber.email].append(post)