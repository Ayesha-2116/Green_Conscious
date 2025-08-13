from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import EventCreationForm, EventRegistrationForm
from django.http import HttpResponse
from MainPage.models import Event
from .models import EventRegistration
import re


# Create your views here.
@login_required
def event_creation(request):
    if request.method == 'POST':
        form = EventCreationForm(request.POST, request.FILES)
        if form.is_valid():
            event_name = form.cleaned_data['event_name']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            event_description = form.cleaned_data['event_description']
            location = form.cleaned_data.get('location')
            image = form.cleaned_data.get('image')
            event_category = form.cleaned_data['event_category']

            e = Event(name=event_name,
                      start_date=start_date,
                      end_date=end_date,
                      description=event_description,
                      created_by=request.user,
                      location=location,
                      image=image,
                      category=event_category)
            e.save()

            return redirect(to='MainPage:main_page')
        else:
            return render(request, 'event_creation.html', {'form': form})
    else:
        form = EventCreationForm()
    return render(request, 'event_creation.html', {'form': form})


@login_required
def event_registration(request, event_id):
    if request.method == 'POST':
        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            #print(request.event.id)
            print(event_id)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone_no']
            event_obj = Event.objects.filter(id=event_id).first()

            # Validate phone number format
            phone_regex = r'^\+?1?\d{9,15}$'
            if not re.match(phone_regex, phone):
                form.add_error('phone_no', "Phone number must be entered in the format: '+999999999'.")
                return render(request, 'event_registration.html', {'form': form, 'event_id': event_id})

            er = EventRegistration(event_id=event_id,
                                   user=request.user,
                                   name=name,
                                   email=email,
                                   phone_number=phone)
            er.save()

            return redirect(to='MainPage:main_page')
    else:
        form = EventRegistrationForm()
    return render(request, 'event_registration.html', {'form': form,
                                                       'event_id': event_id})
