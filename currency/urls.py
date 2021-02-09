from django.urls import path

from . import views

urlpatterns = [
    path('', views.currency_rate, name='currency_rate'),
    path('<int:id>', views.get_rate_by_id, name='get_rate_by_id'),
]
