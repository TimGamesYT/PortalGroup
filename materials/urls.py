from django.urls import path
from . import views

urlpatterns = [
    path('materials/', views.materials_view, name='materials-list'),
    path('create-material/', views.create_material_view, name='create-material'),
    path('delete-material/<int:pk>/', views.delete_material_view, name='delete-material'),
] 
