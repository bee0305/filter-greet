from django.urls import path
from .views import (ProdListView, ProdDetailView)

app_name = 'prods'

urlpatterns = [
    path('', ProdListView.as_view(), name='prods'),
    path('detail/<unid>/', ProdDetailView.as_view(), name='detail')
]
