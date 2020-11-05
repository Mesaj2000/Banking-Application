from django.urls import path
from . import views

urlpatterns = [
    path('send', views.send_money, name='send_money')
]
