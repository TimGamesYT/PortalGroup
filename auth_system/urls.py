from django.urls import path
from . import views

urlpatterns = [
   path("login/", views.login_view, name='login'),
   path("logout/", views.logout_view, name='logout'),
   path("register/", views.register, name='register'),
   path("portfolio/", views.portfolio, name='portfolio'),
   path('edit_portfolio/', views.edit_portfolio, name='edit_portfolio'),
]
