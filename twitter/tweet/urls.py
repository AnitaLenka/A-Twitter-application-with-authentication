from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
    path('tweets/create/', views.tweet_create, name='tweet_create'),
    path('tweets/<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),
    path('tweets/<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('tweet/', views.tweet_list, name='tweet_list_alt'),
]