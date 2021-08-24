from app.views import contact_us
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [

    path('', views.contact_us, name = 'contact_us1'),

            ]
