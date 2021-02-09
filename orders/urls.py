from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_my_orders, name='get_my_orders'),
    path('complete_orders/', views.get_complete_orders, name='get_complete_orders'),
    path('add_order/', views.add_order, name='add_order'),
]
