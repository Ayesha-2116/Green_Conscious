# userhistory/urls.py

from django.urls import path
from .views import user_history

urlpatterns = [
    path('history/', user_history, name='user_history'),
]
