from django.contrib import admin
from .models import ContactForm


@admin.register(ContactForm)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')