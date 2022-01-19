from django import forms
import django_filters as df
from .models import Note, Writer


class NoteFilter(df.FilterSet):
    NOTES_SORT_CHOICES = (
        ('LESS_THAN', 'Less Than'),
        ('GREATER_THAN', 'Greater Than'),
    )

    ORDER_BY_ABC = (
        ('ASC', 'A to Z'),
        ('DESC', 'Z to A'),
    )
    writer = df.CharFilter(
        label="Writer Name",
        field_name="writer__name",
        lookup_expr='icontains',

    )
    number_notes = df.NumberFilter(
        label='Enter amount written notes',
        method='count_total_writer'
    )
    sort_notes_by_abc = df.ChoiceFilter(
        label='Sort notes title by ABC',
        choices=ORDER_BY_ABC,
        method='sort_by_writer'
    )
    writer_sort_notes_by = df.ChoiceFilter(
        label="Sort Number of Books",
        choices=NOTES_SORT_CHOICES,
        method='writer_sort_notes'
    )

    class Meta:
        model = Note
        fields = {
            'title': ['icontains'],
            'status': ['exact']
        }
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.request_data = args[0].dict()
        # print(self.request_data) initials pre-filled
        # {'sort_notes_by_abc': 'ASC', 'number_notes': 1, 'writer_sort_notes_by': 'GREATER_THAN'}

    def sort_by_writer(self, queryset, name, value):
        if value == 'ASC':
            return queryset.order_by('writer__name')
        return queryset.order_by('-writer__name')

    def count_total_writer(self, queryset, name, value):
        """
        all 4 params are required; name= name of the field; value=feature to filter upon
        """
        amount_notes = value
        writers_id = []
        all_writers = Writer.objects.all()
        for wr in all_writers:
            count = Note.objects.filter(writer=wr).count()
            if count >= value:
                writers_id.append(wr.id)
        qs = Note.objects.filter(writer__in=writers_id)
        return qs

    def writer_sort_notes_by (self,queryset,name,value):
        """
        input - initials (view?)
        :param queryset:
        :param name:
        :param value:
        :return:
        """
        return queryset

