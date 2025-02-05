from django.urls import path
from users.views import register, profile, editprofile
from django.contrib.auth import views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('profile/', profile, name='profile'),
    path('password-reset-complete', views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('editprofile/', editprofile, name='editprofile')
]
