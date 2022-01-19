from django.views.generic import ListView
from .filter import NoteFilter
from notes.models import Note


class NoteListFilter(ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'notes/note_list.html'
    paginate_by = 1


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context.update(
        #     filter=NoteFilter(self.request.GET, queryset=self.model.objects.all())
        # )
        notes = NoteFilter(self.request.GET)
        context['filter'] = notes

        return context

    # def get_queryset(self):
    #     qs = self.model.objects.all()
    #     filtered_notes = NoteFilter(self.request.GET, queryset=qs)
    #
    #     return filtered_notes.qs
