from django.urls import path
from django.contrib.auth import views as auth_views
from .auth import LoginView
from . import views

urlpatterns = [
    path('register/', views.register, name='users-register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='users-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='users-logout'),
    path('profile/edit/', views.profile_edit, name='users-profile-edit'),
    path('profile/follow/<int:id>', views.follow_user, name='users-profile-follow'),
    path('profile/unfollow/<int:id>', views.unfollow_user, name='users-profile-unfollow'),

]