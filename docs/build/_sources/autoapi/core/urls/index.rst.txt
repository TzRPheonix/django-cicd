core.urls
=========

.. py:module:: core.urls

.. autoapi-nested-parse::

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





Module Contents
---------------

.. py:data:: router

.. py:data:: urlpatterns

