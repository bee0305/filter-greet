import random
import string
import os

from django.utils.text import slugify
# from prods.models import


def create_unid(num):
    rand_string = string.ascii_letters + string.digits
    collect_chars = [random.choice(rand_string) for _ in range(num)]
    return ''.join(collect_chars)

#
# def create_slug(instance):
#     title = instance.title
#     slug = slugify(title)
#     try:
#         if
#     except:
#         pass

