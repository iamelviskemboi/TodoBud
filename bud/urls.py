from django.urls import path

from . import views

urlpatterns = [
    # Tasks
    path('', views.home, name='home'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    # Profiles
    path('@<str:username>/', views.profile, name='profile'),
    # Feedback
    path('feedback/', views.feedback, name='feedback'),
    path('feedback/thanks/', views.feedback_thanks, name='thanks')
]
