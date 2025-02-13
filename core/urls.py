"""
Configuration des URL pour l'API et l'interface web des tâches.

Routes disponibles :

API REST :
- `GET /tasks/` : Liste toutes les tâches.
- `POST /tasks/` : Ajoute une tâche.
- `GET /tasks/{id}/` : Récupère une tâche spécifique.
- `PUT /tasks/{id}/` : Modifie une tâche.
- `DELETE /tasks/{id}/` : Supprime une tâche.

Interface Web HTMX :
- `GET /tasks/` : Affiche la liste HTML des tâches.
- `POST /tasks/add/` : Ajoute une tâche via HTMX.
- `POST /tasks/update/{id}/` : Modifie une tâche via HTMX.
- `DELETE /tasks/delete/{id}/` : Supprime une tâche via HTMX.
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, task_list, task_create, task_delete, task_update

# ✅ API REST avec Django REST Framework
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

# ✅ Routes HTML et API
urlpatterns = [
    path("tasks/", task_list, name="task-list"),  # Page HTML avec les tâches
    path("tasks/add/", task_create, name="task-create"),  # Ajout d'une tâche via HTMX
    path("tasks/delete/<int:task_id>/", task_delete, name="task-delete"),  # Suppression
    path("tasks/update/<int:task_id>/", task_update, name="task-update"),  # Modification
    path("", include(router.urls)),  # API REST
]
