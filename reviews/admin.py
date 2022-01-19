from django.contrib import admin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user','prod','text','created_at',)
    list_filter = ('prod',('created_at',DateRangeFilter),('updated_at',DateTimeRangeFilter),'user__last_name')

admin.site.register(Review,ReviewAdmin)