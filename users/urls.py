from django.urls import path
from . import views

urlpatterns = [
    path('settings', views.user_settings, name='user_settings'),
    path('logout', views.user_logout, name='user_logout'),
]
