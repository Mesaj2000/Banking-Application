"""bankapp_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


# this is how Django knows which files are loaded to which URLs in the app.
# this is the main urls.py for the whole project, so it has to include the
# url files for all the other smaller segments
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication_system.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('view_balances.urls')),
    path('', include('send_money.urls')),
    path('', include('transaction_history.urls')),
    path('', include('settings_page.urls')),
    path('', include('request_money.urls'))
]
