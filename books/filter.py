import django_filters
from django.db.models import F
from django.forms.widgets import RadioSelect, Select

from .models import Book


# Lets compare this filter with REST

class BookFilter(django_filters.FilterSet):
    ABC_CHOICES = (
        ('ascending', 'A-z'),
        ('descending', 'Z-a')
    )
    RATING_CHOICES = (
        ('ascending', 'min top'),
        ('descending', 'max top')

    )

    title = django_filters.CharFilter(lookup_expr='icontains')
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    ordering_abc = django_filters.ChoiceFilter(
        empty_label='Select by A-Z',
        label='ABC Ordering',
        choices=ABC_CHOICES,
        # widget=SelectMultiple,
        widget=Select(choices=ABC_CHOICES),
        method='filter_by_abc')

    price_ord = django_filters.ChoiceFilter(
        empty_label='Select by Price',
        label='Price Order',
        choices=RATING_CHOICES,
        widget=Select(choices=RATING_CHOICES),
        method='filter_by_price')

    rating_ord = django_filters.ChoiceFilter(
        empty_label='Select by Max Rating',
        label='Rating Max',
        choices=RATING_CHOICES,
        widget=Select(choices=RATING_CHOICES),
        method='filter_by_max_rating')

    rating_average = django_filters.ChoiceFilter(
        empty_label='Select by Avg Rating',
        label='Rating AVG',
        choices=RATING_CHOICES,
        widget=Select(choices=RATING_CHOICES),
        method='filter_by_avg_rating')

    def filter_by_abc(self, queryset, name, value):
        expression = 'title' if value == 'ascending' else '-title'
        return queryset.order_by(expression)

    def filter_by_price(self, queryset, name, value):
        expression = 'price' if value == 'ascending' else '-price'
        return queryset.order_by(expression)

    def filter_by_max_rating(self, queryset, name, value):
        '''queryset = Book.objects.order_by(F('max_rating').desc(nulls_last=True))
        print(str(Book.objects.values('max_rating').order_by(F('max_rating').desc(nulls_last=True)).query))
        expression = '-max_rating' if value == 'descending' else 'max_rating'
        print(queryset.order_by(expression))
        print(queryset.order_by(expression).query)
        return queryset.order_by(expression) '''
        # see below
        return queryset.order_by(F('max_rating').desc(nulls_last=True)) \
            if value == 'descending' else queryset.order_by('max_rating')
        

    def filter_by_avg_rating(self, queryset, name, value):
        if value == 'descending':
            # eqivalent -avg_rate? 
            return queryset.order_by(F('avg_rate').desc(nulls_last=True))
        return Book.objects.order_by(F('avg_rate'))

    class Meta:
        model = Book
        # let op: don't include fields don't belong to the model
        # TypeError: 'Meta.fields' must not contain non-model field names: price__lt
        fields = ['title']


"""
    avg_rate = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    an_likes = models.IntegerField(null=True, blank=True)
    max_rating = models.DecimalField(null=True, decimal_places=2, max_digits=5, blank=True)
    
    raw query: 
    SELECT * FROM  .... ORDER BY max_rating DESC NULLS LAST   
     
    str(...).query
    SELECT "books_book"."max_rating" FROM "books_book" 
    ORDER BY "books_book"."max_rating" DESC NULLS LAST

"""
