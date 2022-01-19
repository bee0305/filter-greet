from django.http import Http404
from django.views.generic import ListView, DetailView
from django.core.exceptions import MultipleObjectsReturned
# from analytics.mixins import ObjectViewedMixin
from products.models import Product
from .filters import ProductFilter


class ProdListView(ListView):
    """
    GET /?title=kersen&ordering=ascending&categ__name=&price__lt=120&price__gt=
    """
    model = Product
    context_object_name = 'prods'
    template_name = 'products/product_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        print(self.request.GET)
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        return context

# ObjectViewedMixin,
class ProdDetailView(DetailView):
    model = Product
    context_object_name = 'prod'
    template_name = 'products/product_detail.html'

    def get_object(self, queryset=None):
        unid = self.kwargs.get('unid')
        print("unid", unid)
        try:
            instance = Product.objects.get(unid=unid)
        except Product.DoesNotExist:
            raise Http404('Product not found')
        except MultipleObjectsReturned:
            qs = Product.objects.filter(unid=unid)
            instance = qs.first()
        except:
            raise Http404('Product not found')
        return instance
