from django.urls import path
from . import views

# Adds the "view_balances" view to the "/balances" path
urlpatterns = [
    path('balances', views.view_balances, name='view_balances')
]
