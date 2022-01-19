from django.db import models
from timestamp.models import TimeStamp


class Writer(TimeStamp):
    name = models.CharField(max_length=120)

    @property
    def get_notes_count(self):
        return Note.objects.filter(writer=self.id).count()
        # return self.notes.count()?

    def __str__(self):
        return self.name


class Note(TimeStamp):
    NOTE_STATUS = (
        ('PUB', 'Published'),
        ('ON_HOLD', 'On Hold')
    )
    title = models.CharField(max_length=120)
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE, related_name='notes')
    status = models.CharField(max_length=24, choices=NOTE_STATUS)


    # obj.get_status_display
    # do you need it? (see below?)
    # @property
    # def get_human_status(self):
    #     for row in range(0,2):
    #         if self.NOTE_STATUS[row][0]== self.status:
    #             status_ = self.NOTE_STATUS[row][1]
    #             break
    #     return status_

    def __str__(self):
        return f'{self.title} by {self.writer} (id={self.id}) '

