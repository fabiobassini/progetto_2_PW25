"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from core import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    # Clienti
    path("clienti/", views.cliente_list, name="cliente_list"),
    path("clienti/nuovo/", views.cliente_create, name="cliente_create"),
    path("clienti/<int:pk>/modifica/", views.cliente_edit, name="cliente_edit"),
    path("clienti/<int:pk>/elimina/", views.cliente_delete, name="cliente_delete"),
    # Utenze
    path("utenze/", views.utenza_list, name="utenza_list"),
    # Fatture & Letture
    path("fatture/", views.fattura_list, name="fattura_list"),
    path("letture/", views.lettura_list, name="lettura_list"),
]
