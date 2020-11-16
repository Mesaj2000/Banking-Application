from django.urls import path
from . import views

# Loads the "settings_page" view at the "/settings_page" URL
urlpatterns = [
    path('settings_page', views.settings_page, name='settings_page')
]
