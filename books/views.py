from django.db.models import F
from django.shortcuts import render
from django.views.generic import ListView

from books.models import Book
from .filter import BookFilter


class BookListFilter(ListView):
    """
    GET /?title=kersen&ordering=ascending&categ__name=&price__lt=120&price__gt=
    """
    model = Book
    context_object_name = 'books'
    template_name = 'books/book_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        print(self.request.GET)
        context = super().get_context_data(**kwargs)
        context['filter'] = BookFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        return Book.objects.order_by(F('max_rating').desc(nulls_last=True))
