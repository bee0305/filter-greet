import uuid
from django.db import models

from autoslug import AutoSlugField
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=120)
    slug = AutoSlugField(populate_from='name', unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True,
                            blank=True, db_index=True, related_name='children'
                            )

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = 'name'

    class Meta:
        unique_together = (('parent', 'slug'),)
        verbose_name_plural = 'categories'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Product(models.Model):
    arrived_at = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from='title', unique=True)
    unid = models.UUIDField(default=uuid.uuid4, editable=False)
    description = models.TextField()
    categ = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='prods')
    stock = models.BooleanField(default=True)
    new = models.BooleanField(default=False)
    sale = models.BooleanField(default=False)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
