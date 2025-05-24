from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('calendar/', views.calendar_view, name='calendar'),
    path('add/', views.create_event, name='add_event'),
    path('delete/<int:event_id>/', views.delete_event, name='delete_event'),  # 🆕
]
