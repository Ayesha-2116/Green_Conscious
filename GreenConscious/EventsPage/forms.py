from django import forms
from django.core.exceptions import ValidationError
import datetime
from django.utils import timezone
from pygments.lexer import default

from MainPage.models import EventCategory


class EventCreationForm(forms.Form):
    event_name = forms.CharField(required=True,
                                 label='Event Name',
                                 widget=forms.TextInput(attrs={'class': 'input_field',
                                                               'placeholder': 'Please enter event name'}))
    event_description = forms.CharField(required=True,
                                        label='Event Description',
                                        widget=forms.Textarea(attrs={'class': 'form-control',
                                                                     'placeholder': 'Please enter event description'}))
    start_date = forms.DateField(required=True,
                                 label='Event Start Date',
                                 widget=forms.DateInput(attrs={'type': 'date', 'class': 'dateTime_field'}),
                                 initial=datetime.date.today)
    end_date = forms.DateField(required=True,
                               label='Event End Date',
                               widget=forms.DateInput(attrs={'type': 'date', 'class': 'dateTime_field'}))

    image = forms.ImageField(required=False,
                             label='Event Image',
                             widget=forms.ClearableFileInput())

    location = forms.CharField(required=True,
                               label='Event Location',
                               widget=forms.TextInput(attrs={'class': 'input_field',
                                                             'placeholder': 'Please enter location'}))

    event_category = forms.ModelChoiceField(queryset=EventCategory.objects.all(),
                                            label='Event Category',
                                            empty_label=None,
                                            widget=forms.Select(attrs={'class': 'input_field'}))

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date:
            if end_date < start_date:
                raise ValidationError({'end_date': 'End date cannot be before start date.'})

            today = timezone.now().date()
            if start_date < today:
                raise ValidationError({'start_date': 'Start date cannot be in the past.'})
            if end_date < today:
                raise ValidationError({'end_date': 'End date cannot be in the past.'})

        return cleaned_data


class EventRegistrationForm(forms.Form):
    name = forms.CharField(required=True,
                           label='Name',
                           widget=forms.TextInput(attrs={'class': 'input_field',
                                                         'placeholder': 'Please enter your name'}))
    email = forms.EmailField(required=True,
                             label='Email',
                             widget=forms.TextInput(attrs={'class': 'input_field',
                                                           'placeholder': 'Please enter your email'}))
    phone_no = forms.CharField(required=True,
                               label='Phone Number',
                               widget=forms.TextInput(attrs={'class': 'input_field',
                                                             'placeholder': 'Please enter your phone no.'}))
