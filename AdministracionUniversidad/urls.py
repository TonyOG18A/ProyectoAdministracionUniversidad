from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('formularioContacto/', views.formularioContacto, name="formularioContacto"),
    path('contactar/', views.contactar, name="contactar")
]