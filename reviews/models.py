from django.db import models
from django.contrib.auth import get_user_model
from timestamp.models import TimeStamp
from products.models import Product

User = get_user_model()


class Review(TimeStamp):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_review')
    text = models.TextField()
    prod = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'review for {self.prod.title}'
