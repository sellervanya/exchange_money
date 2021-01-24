from django.urls import path
from . import views

urlpatterns = [
    path('', views.currency_rate, name='currency_rate'),
]
