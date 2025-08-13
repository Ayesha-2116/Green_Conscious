# forms.py in VolunteerMatching app
import datetime

from django import forms
from Login_SignUp.models import UserProfile
from MainPage.models import Event, EventCategory


class VolunteerMatchingForm(forms.Form):
    userEventInterested = forms.ModelChoiceField(
        queryset=EventCategory.objects.all(),
        label='Select Interest',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    date = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}), initial=datetime.date.today)
