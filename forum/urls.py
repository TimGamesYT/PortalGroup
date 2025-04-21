from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum, name='forum'),
    path('create-post/', views.create_post_view, name='create-post'),
    path('edit-post/<int:pk>/', views.edit_post_view, name='edit-post'),
    path('delete-post/<int:pk>/', views.delete_post_view, name='delete-post'),
    path('<int:pk>/', views.post_detail, name='post-detail'),
    path('create-comment/<int:pk>/', views.create_comment_view, name='create-comment'),
    path('edit-comment/<int:pk>/', views.edit_comment_view, name='edit-comment'),
    path('delete-comment/<int:pk>/', views.delete_comment_view, name='delete-comment'),
]