from django.urls import path
from . import views

urlpatterns = [
   # path('login/', views.login, name='login-page'),
    path('about/', views.about, name='about-page'),
    path('my_profile/', views.profile, name='profile-page'),
    path('', views.home, name='home-page'),
]