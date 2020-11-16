from django.urls import path
from . import views

# Adds the "index" view to the "/" path
# Adds the "register" view to the "/register" path
urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register')
]
