"""
Configuration des URL pour le projet Django-CI/CD.

Ce module définit les routes principales du projet.

Routes :
    - **`/admin/`** : Interface d'administration Django.
    - **`/`** : Inclusion des routes définies dans `core.urls`.

"""
from django.urls import path, include
from core.views import home

urlpatterns = [
    path("", home, name="home"),  # Page d'accueil
    path("", include("core.urls")),
]
