from django.urls import path
from . import views

urlpatterns = [
    path('', views.volunteer_matching, name='volunteer_matching'),
]
