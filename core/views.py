"""
Module des vues pour l'API et l'interface web des tâches.

Ce module définit :
1️⃣ Un **ViewSet API REST** basé sur Django REST Framework.
2️⃣ Une **interface HTML** améliorée avec HTMX pour un CRUD dynamique.
"""

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer


# ✅ 1️⃣ API REST avec Django REST Framework
class TaskViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les tâches via l'API REST.

    Routes disponibles :
    - **GET /tasks/** : Liste toutes les tâches.
    - **POST /tasks/** : Crée une nouvelle tâche.
    - **GET /tasks/{id}/** : Récupère une tâche spécifique.
    - **PUT /tasks/{id}/** : Met à jour une tâche existante.
    - **DELETE /tasks/{id}/** : Supprime une tâche.
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

def home(request):
    """Page d'accueil avec un menu de navigation."""
    return render(request, "core/home.html")

# ✅ 2️⃣ Interface Web - Afficher la Liste des Tâches
def task_list(request):
    """
    Affiche une page HTML avec toutes les tâches sous forme de liste.

    Cette vue retourne un rendu HTML et est utilisée avec HTMX pour
    un CRUD dynamique.
    """
    tasks = Task.objects.all()
    return render(request, "core/task_list.html", {"tasks": tasks})


# ✅ 3️⃣ Interface Web - Ajouter une Tâche via HTMX
@csrf_exempt
def task_create(request):
    """
    Ajoute une nouvelle tâche avec HTMX.

    Cette vue renvoie un template HTML partiel contenant la tâche ajoutée.
    """
    if request.method == "POST":
        title = request.POST.get("title", "")
        if title:
            task = Task.objects.create(title=title)
            return render(request, "core/task_item.html", {"task": task})
    return HttpResponse(status=400)


# ✅ 4️⃣ Interface Web - Supprimer une Tâche via HTMX
@csrf_exempt
def task_delete(request, task_id):
    """
    Supprime une tâche et met à jour la liste, sans recréer le conteneur principal.
    """
    task = get_object_or_404(Task, id=task_id)
    task.delete()

    if "HX-Request" in request.headers:
        tasks = Task.objects.all()
        return render(request, "core/task_list_partial.html", {"tasks": tasks})  # ✅ Nouveau template PARTIEL

    return HttpResponse("", status=204)  # ✅ Retour par défaut si ce n'est pas HTMX



# ✅ 5️⃣ Interface Web - Modifier une Tâche via HTMX
@csrf_exempt
def task_update(request, task_id):
    """
    Met à jour une tâche existante avec HTMX.

    - `GET` : Affiche le formulaire d'édition.
    - `POST` : Enregistre la modification et affiche la tâche mise à jour.
    """
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        if title:
            task.title = title
            task.save()
            return render(request, "core/task_item.html", {"task": task})
        return HttpResponse(status=400)  # Si titre vide

    return render(request, "core/task_edit.html", {"task": task})
