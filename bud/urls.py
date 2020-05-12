from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('insert/', views.insert, name='insert'),
    path('delete/<int:todo_id>', views.delete, name='delete'),
]
