from django.urls import path
from django.views.generic import TemplateView
from .views import contact_view

urlpatterns = [
    path('', contact_view, name='contact_form'),
    path('success/', TemplateView.as_view(template_name='contact_success.html'), name='contact_success'),
]