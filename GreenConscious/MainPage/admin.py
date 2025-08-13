from django.contrib import admin
from .models import Event, EventCategory


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'created_by')


@admin.register(EventCategory)
class EventCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_events')

    def total_events(self, obj):
        return obj.total_events

    total_events.short_description = 'Total events'