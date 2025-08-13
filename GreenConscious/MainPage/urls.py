from django.urls import path
from . import views

app_name = 'MainPage'

urlpatterns = [
    path('home/', views.main_page, name='main_page'),
    path('home/myevents/', views.myEvents, name='myevents'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('event_update/<int:event_id>/', views.event_update, name='event_details_update'),
    path('past_events/', views.past_events, name='past_events'),  # Add this line
    path('event_delete/<int:event_id>/', views.event_delete, name='event_delete'),
    path('cancel_registration/<int:event_id>/', views.cancel_registration, name='cancel_registration'),
]
