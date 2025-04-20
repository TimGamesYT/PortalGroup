from django.urls import path
from .views import LoginView, Logout

urlpatterns = [
   path("login/" ,LoginView, name='login'),
   path("logout/" ,Logout, name='logout'),
#   path("book-room", book_room, name='book_room')
]

