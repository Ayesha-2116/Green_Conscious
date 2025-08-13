from django.contrib import admin
from .models import EventRegistration
# Register your models here.



@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'name', 'email', 'phone_number')
