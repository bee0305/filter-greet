from decimal import Decimal

from django.db.models import Avg, Case, Count, Max, When

from .models import UserBookRelation


def calc_rating(obj):
    rating_val = UserBookRelation.objects.filter(book=obj).aggregate(rate_value=(Avg('rating')))
    obj.avg_rate = rating_val.get('rate_value', None)
    obj.save()


def calc_count_likes(obj):
    agr_likes = UserBookRelation.objects.filter(book=obj).aggregate(like_total=(Count(Case(When(like=True, then=1)))))
    obj.an_likes = agr_likes.get('like_total', None)
    obj.save()


def calc_max_rating(obj):
    max_rate = UserBookRelation.objects.filter(book=obj).aggregate(max_rating=Max('rating'))
    obj.max_rating = Decimal(max_rate.get('max_rating', None))
    obj.save()