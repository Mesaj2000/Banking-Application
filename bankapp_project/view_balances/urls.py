from django.urls import path
from . import views

urlpatterns = [
    path('balances', views.view_balances, name='view_balances')
]
