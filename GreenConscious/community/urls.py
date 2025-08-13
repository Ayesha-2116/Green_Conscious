from django.urls import path
from . import views

urlpatterns = [
    path('', views.community_page, name='community_page'),
    path('create/', views.create_post, name='create_post'),
]
