import django_filters
from django.forms.widgets import RadioSelect, TextInput,Select
from django.core.paginator import Paginator

from .models import Product, Category


class ProductFilter(django_filters.FilterSet):
    ABC_CHOICES = (
        ('ascending', 'A-z'),
        ('descending', 'Z-a')
    )
    SALE_CHOICES = (('1', 'Sale'),
                    ('0', 'No sale'),
                    (None, 'Сброс')
                    )
    ordering = django_filters.ChoiceFilter(
        empty_label='Select by A-Z',
        label='Ordering',
        choices=ABC_CHOICES,
        # widget=SelectMultiple,
        widget=Select(choices=ABC_CHOICES),
        method='filter_by_order')
    title = django_filters.CharFilter(lookup_expr='icontains')
    categ = django_filters.ChoiceFilter(
        empty_label="choose categs",
        label="cats")
    sale = django_filters.BooleanFilter(
        field_name='sale',
        widget=RadioSelect(
            # attrs={'class': 'form-control col-lg-4'},
            choices=SALE_CHOICES
        )
    )


    class Meta:
        model = Product
        fields = ['title', 'sale', 'price', 'categ']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form.fields['categ'].choices = self.categs_lst()
        # print(args) == tuple==(<QueryDict: {'title': [''],.... 'price': [''], 'categ': ['2']}>,)
        self.request_data = args[0].dict()  # {'title': '', 'sale': '', 'price': '', 'categ': '2'}

    def filter_by_order(self, queryset, name, value):
        expression = 'title' if value == 'ascending' else '-title'
        return queryset.order_by(expression)

    def categs_lst(self):
        lst = []
        for categ in Category.objects.all():
            lst.append([categ.id, categ.name])
        # print('lst is:', lst)
        return lst

