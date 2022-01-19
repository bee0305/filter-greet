from django.urls import path
from .views import ReviewCreateView,ReviewDetailView

app_name = 'reviews'

urlpatterns = [
    path('create/', ReviewCreateView.as_view(), name='create-review'),
    path('detail/<int:pk>/', ReviewDetailView.as_view(), name='detail-review'),
]