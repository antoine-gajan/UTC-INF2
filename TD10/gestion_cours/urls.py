from django.urls import path

from . import views

urlpatterns = [
    path('', views.base, name="base"),
    path('cours/new', views.creer_cours, name="creer_cours"),
]