"""
Configuration des URL pour le projet Django-CI/CD.

Ce module définit les routes principales du projet.

Routes :
    - **`/admin/`** : Interface d'administration Django.
    - **`/`** : Inclusion des routes définies dans `core.urls`.

Exemple d'utilisation :
    >>> from django.urls import path, include
    >>> urlpatterns = [
    ...     path('admin/', admin.site.urls),
    ...     path('', include('core.urls')),
    ... ]
"""

from django.contrib import admin
from django.urls import path, include
from core.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),  # Page d'accueil
    path("tasks/", include("core.urls")),  # Gestion des tâches
]

