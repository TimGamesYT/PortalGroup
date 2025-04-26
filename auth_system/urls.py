from django.urls import path
from . import views

urlpatterns = [
   path("", views.homepage, name='homepage'),
   path("novations/", views.novations, name='novations'),
   path("announs/", views.announs, name='announs'),
   path("login/", views.login_view, name='login'),
   path("logout/", views.logout_view, name='logout'),
]
