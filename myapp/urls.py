from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create', views.create, name='create_todo'),
    path('edit/<str:pk>/', views.edit, name='edit_todo'),
    path('delete/<str:pk>/', views.delete, name='delete_todo')
]