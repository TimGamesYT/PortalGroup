from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='quiz'),
    path('<int:question_id>/', views.question_detail, name='question_detail'),
]