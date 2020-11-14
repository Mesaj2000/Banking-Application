from django.urls import path
from . import views

# Adds the "request_money" view to the "/request_money" path
# and the "view_requests" view to the "/view_requests" path
urlpatterns = [
    path('request_money', views.request_money, name='request_money'),
    path('view_requests', views.view_requests, name='view_requests')
]
