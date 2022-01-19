import django_filters
from django.forms.widgets import TextInput, RadioSelect  # ,SelectMultiple
from .models import Product, Category


class ProductFilter(django_filters.FilterSet):
    CHOICES = (
        ('ascending', 'A-z'),
        ('descending', 'Z-a')
    )

    title = django_filters.CharFilter(lookup_expr='icontains')
    # price__gt = django_filters.NumberFilter(
    #     field_name='price', lookup_expr='gt',
    #     )
    #     # label='price max', widget=TextInput(attrs={'placeholder': 'max'}))
    #
    # price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    # ordering = django_filters.ChoiceFilter(
    #     empty_label='Select by A-Z',
    #     label='Ordering',
    #     choices=CHOICES,
    #     # widget=SelectMultiple,
    #     widget=RadioSelect,
    #     method='filter_by_order')
    # categ = django_filters.ChoiceFilter(
    #     empty_label="categories",
    #     label="cats")

    class Meta:
        model = Product

        fields = ['title','sale'] #, 'ordering', 'categ', 'price__lt', 'price__gt']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args,**kwargs)
    #     for field in self.form.fields.values():
    #         field.widget.attrs={'class':'col-lg-6'}
    #     self.form.fields['categ'].choices = self.categs_lst()
    #     self.request_data = args[0].dict() # what's this?

    # def filter_by_order(self, queryset, name, value):
    #     expression = 'title' if value == 'ascending' else '-title'
    #     return queryset.order_by(expression)
    #
    def categs_lst(self):
        lst = []
        for categ in Category.objects.all():
            lst.append([categ.id, categ.name])
        return lst
