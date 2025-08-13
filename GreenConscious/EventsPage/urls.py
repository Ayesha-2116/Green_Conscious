from django.urls import path

import MainPage.views
from . import views

app_name = 'EventsPage'

urlpatterns = [
    path('', views.event_creation, name='event_creation'),
    path('event_creation/', views.event_creation, name='event_creation'),
    path('event_registration/<int:event_id>/', views.event_registration, name='event_registration'),
    path('main_page/', MainPage.views.main_page, name='main_page'),
]