from django.contrib.auth.models import User
from django.db import models
from django.core.cache import cache

from django.db.models import Sum


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE())
    ratingAuthor = models.SmallIntegerField(default=0)

    def update_rating(self):
        post_rating = self.post_set.aggregate(Sum('rating')).get('rating_sum')
        if post_rating is None:
            post_rating = 0

        compost_rating = 0
        for post in self.post_set.all():
            rating = post.comment_set.aggregate(Sum('rating')).get('rating_sum')
            if rating is None:
                rating = 0
            compost_rating += rating

        self.rating = post_rating
        self.save()

    def __str__(self):
        return f'{self.authorUser.username}'


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE())

    Tanks = 'TA'
    Hills = 'HI'
    DD = 'DD'
    Merchants = 'ME'
    Guildmasters = 'GU'
    Questgivers = 'QU'
    Blacksmiths = 'BS'
    Leatherworkers = 'LW'
    Potionsmasters = 'PM'
    Spellmasters = 'SM'
    Category_Choices = (
        (Tanks, 'Танки'),
        (Hills, 'Хилы'),
        (DD, 'ДД'),
        (Merchants, 'Торговцы'),
        (Guildmasters, 'Гилдмастеры'),
        (Questgivers, 'Квестгиверы'),
        (Blacksmiths, 'Кузнецы'),
        (Leatherworkers, 'Кожевники'),
        (Potionsmasters, 'Зельевары'),
        (Spellmasters, 'Мастера заклинаний'),
    )

    categoryType = models.CharField(max_length=2, choices=Category_Choices)
    dateCreation = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=128)
    text = models.TextField()
    image = models.ImageField(upload_to=None, height_field=None, width_field=None,max_length=100)
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return '{} ... {}'.format(self.text[0:128], str(self.rating))

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f'post-{self.pk}')


class Review(models.Model):
    reviewPost = models.ForeignKey(Post, on_delete=models.CASCADE())
    reviewUser = models.ForeignKey(User, on_delete=models.CASCADE())
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None,max_length=100)

