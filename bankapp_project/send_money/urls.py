from django.urls import path
from . import views

# Adds the "send_money" view to the "/send" path
urlpatterns = [
    path('send', views.send_money, name='send_money')
]
