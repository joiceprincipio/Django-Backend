from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todos, name='todos'),  
    path('update/<int:pk>/', views.update, name='update'),  
]
