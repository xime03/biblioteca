"""Pag_Biblioteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Pag_Biblioteca.Vista import inicio
from Pag_Biblioteca.Vista import reservar
from Pag_Biblioteca.Vista import borrar
from Pag_Biblioteca.Vista import ingresar
from Pag_Biblioteca.Vista import pedir
from Pag_Biblioteca.Vista import registrar
from Pag_Biblioteca.Vista import ver
 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^inicio/$', inicio),
    url(r'^reservar/$', reservar),
    url(r'^borrar/$', borrar),
    url(r'^ingresar/$', ingresar),
    url(r'^pedir/$', pedir),
    url(r'^registrar/$', registrar),
    url(r'^ver/$', ver),
]
