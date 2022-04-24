from django.urls import path
from . import views

urlpatterns = [
    path('my_profile/', views.profile, name='profile-page'),
    path('', views.home, name='home-page'),
    path('<id>/update', views.update_task, name='update'),
    path('<id>/delete', views.delete_task, name='delete'),
    path('edit_profile/', views.update_profile, name='edit-profile'),
]
