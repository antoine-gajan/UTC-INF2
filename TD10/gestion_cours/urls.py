from django.urls import path

from . import views

urlpatterns = [
    path('', views.base, name="base"),
    path('cours/', views.afficher_cours, name="afficher_cours"),
    path('cours/new', views.creer_cours, name="creer_cours"),
    path('etudiants/', views.afficher_etudiants, name="afficher_etudiants"),
    path('etudiants/new', views.creer_etudiant, name="creer_etudiant")
]