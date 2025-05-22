from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_list, name='survey'),
    path('<int:question_id>/', views.question_detail, name='question_detail'),
]