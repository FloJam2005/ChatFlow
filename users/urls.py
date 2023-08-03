from django.contrib.auth import views as auth_views
from django.urls import path

import users
import users.views as user_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', user_views.register, name='register'),
    path('profile/<str:username>', users.views.user_profile, name="user-profile-page"),
    path("profile/edit/<int:pk>", user_views.UserUpdateView.as_view(), name="user-update"),
    path("profile/<str:username>/follow", user_views.userFollow, name="user-follow")

]
