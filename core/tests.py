import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from core.models import Task


@pytest.mark.django_db
def test_get_empty_task_list():
    client = APIClient()
    url = reverse("task-list")

    response = client.get(url, format="json", HTTP_ACCEPT="application/json")

    assert response.status_code == 200
    assert response.headers["Content-Type"].startswith("application/json")
    assert response.json() == []

@pytest.mark.django_db
def test_create_task():
    client = APIClient()
    url = reverse("task-list")

    data = {"title": "Nouvelle tâche", "description": "Test CI/CD", "completed": False}
    response = client.post(url, data, format="json", HTTP_ACCEPT="application/json")

    assert response.status_code in [200, 201]
    assert Task.objects.count() == 1



@pytest.mark.django_db
def test_get_specific_task():
    client = APIClient()
    task = Task.objects.create(title="Tâche Test", description="Détails de la tâche", completed=False)
    url = reverse("task-detail", kwargs={"pk": task.id})

    response = client.get(url)

    assert response.status_code == 200
    assert response.json()["title"] == "Tâche Test"


@pytest.mark.django_db
def test_update_task():
    client = APIClient()
    task = Task.objects.create(title="Tâche Initiale", description="À modifier", completed=False)
    url = reverse("task-detail", kwargs={"pk": task.id})

    updated_data = {"title": "Tâche Modifiée", "description": "Mise à jour CI/CD", "completed": True}
    response = client.put(url, updated_data, format="json")

    task.refresh_from_db()

    assert response.status_code == 200
    assert task.title == "Tâche Modifiée"
    assert task.completed is True


@pytest.mark.django_db
def test_delete_task():
    """OUAAAAAAAAAAAAAAAAAAAAAIS."""
    client = APIClient()
    task = Task.objects.create(title="Tâche à Supprimer", description="Doit être supprimée", completed=False)
    url = reverse("task-detail", kwargs={"pk": task.id})

    response = client.delete(url)

    assert response.status_code == 204
    assert Task.objects.count() == 0
