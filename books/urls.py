from django.urls import path
from .views import BookListFilter

app_name = 'books'

urlpatterns = [
    path('', BookListFilter.as_view(), name="list"),

]
