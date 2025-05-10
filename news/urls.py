from django.urls import path
from . import views

urlpatterns = [
   path("novations/", views.NovationsListView.as_view(), name='novations'),
   path("announs/", views.AnnounsListView.as_view(), name='announs'),
]