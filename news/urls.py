from django.urls import path
from . import views

urlpatterns = [
   path("novations/", views.novations, name='novations'),
   path("announs/", views.announs, name='announs'),
]