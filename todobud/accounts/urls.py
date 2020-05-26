from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # Authentication & Registration
    path('login/', views.sign_in, name='login'),
    path('logout/', views.sign_out, name='logout'),
    path('register/', views.register, name='register'),
    path('<str:username>/settings/', views.settings, name='settings'),
    # Password Reset
    path('password/reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),
         name='reset_password'),
    path('password/reset/sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'),
         name='password_reset_done'),
    path('password/reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'),
         name='password_reset_confirm'),
    path('password_reset/success/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_success.html'),
         name='password_reset_complete')
]
