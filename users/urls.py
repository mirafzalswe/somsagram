from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("singup/", views.register, name='users-register'),
    path("login/", auth_views.LoginView.as_view(template_name='users/login.html'), name='users-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='users-logout'),
    path('profile/', views.profile, name='users-profile'),
    path('about/', views.about, name='users-about'),
    path('update/', views.update_profile, name='update-profile'),
    path('my-posts/', views.my_posts, name='my-posts')

]
