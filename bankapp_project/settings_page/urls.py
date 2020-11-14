from django.urls import path
from . import views

urlpatterns = [
    path('settings_page', views.settings_page, name='settings_page')
]
