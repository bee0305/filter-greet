from django.db import models
from django.contrib.auth import get_user_model
from autoslug import AutoSlugField

from timestamp.models import TimeStamp

User = get_user_model()


class Author(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Book(TimeStamp):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=240)
    slug = AutoSlugField(populate_from='title', unique=True)
    lead_text = models.CharField(max_length=254, default="")
    view_count = models.IntegerField(blank=True, default=0)
    featured = models.BooleanField(blank=True, default=False)
    fans = models.ManyToManyField(User, related_name='book_fans', through='UserBookRelation')

    price = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True, default="0.00")
    avg_rate = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    an_likes = models.IntegerField(null=True, blank=True)
    max_rating = models.DecimalField(null=True, decimal_places=2, max_digits=5, blank=True)

    def __str__(self):
        return self.title


class UserBookRelation(models.Model):
    """ if attr rating or like get updated cached fields in idea model will be also re-calculated """
    RATING = (
        (1, 'OK'),
        (2, 'Fine'),
        (3, 'Good'),
        (4, 'Amazing'),
        (5, 'Excellent')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    like = models.BooleanField(blank=True, default=False)
    dislike = models.BooleanField(blank=True, default=False)
    in_bookmark = models.BooleanField(blank=True, default=False)
    rating = models.PositiveSmallIntegerField(choices=RATING, null=True, blank=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.old_rating = self.rating
        self.old_like = self.like

    def __str__(self):
        return f'User: {self.user} active in user-idea-relations {self.like}, {self.rating}'

    def save(self, *args, **kwargs):
        """ import here: to avoid circular import (idea-user-relation calls idea-user-relation)"""
        from .calc import calc_count_likes, calc_max_rating, calc_rating

        # if like or rating changed |=> re-calc total likes on idea
        start_creating = not self.pk
        super().save(*args, **kwargs)  # here idea gets (if triggered by change rating event)
        new_rating = self.rating
        new_like = self.like

        if self.old_rating != new_rating or start_creating:
            # obj is already exist,so working on condition old != new
            calc_rating(self.book)
            calc_max_rating(self.book)

        if self.old_like != new_like or start_creating:
            # user-idea-rel obj is just created
            calc_count_likes(self.book)
