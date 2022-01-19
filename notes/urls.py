from django.urls import path
from .views import NoteListFilter

app_name = 'notes'

urlpatterns = [
    path('', NoteListFilter.as_view(), name="list"),

]
