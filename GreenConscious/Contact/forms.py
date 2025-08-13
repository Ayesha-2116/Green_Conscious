from django import forms
from .models import ContactForm as ContactFormModel


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactFormModel
        fields = ['name', 'email', 'subject', 'message']
