from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),         
    path('logout/', views.logoutUser, name='logout'),         
    path('logout/', views.registerPage, name='register'),         

    path('', views.home, name='home'),
    path('room/<pk>/', views.room, name='room'),
    
    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<pk>/', views.updateRoom, name='update-room'),
    path('delete-room/<pk>/', views.deleteRoom, name='delete-room'),
]