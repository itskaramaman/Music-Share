from django.urls import path
from . import views

urlpatterns = [
    path('', views.endpoints),
    path('room-list/', views.room_list, name='room-list')
]
