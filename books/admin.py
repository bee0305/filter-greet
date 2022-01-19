from django.contrib import admin
from .models import Author, Book, UserBookRelation

from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'price', 'author', 'avg_rate', 'an_likes', 'max_rating']

    class Meta:
        model = Book


admin.site.register(Author)
admin.site.register(Book, BookAdmin)
admin.site.register(UserBookRelation)

# Register your models here.
