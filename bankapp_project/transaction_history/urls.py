from django.urls import path
from . import views

# Adds the "transaction_hisstory" view to the "/transaction_history" path
urlpatterns = [
    path('transaction_history', views.transaction_history,
         name='transaction_history')
]
