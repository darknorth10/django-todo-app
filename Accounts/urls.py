from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register-page'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login-page'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout-page'),
]