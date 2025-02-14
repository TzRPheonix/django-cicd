core.views
==========

.. py:module:: core.views

.. autoapi-nested-parse::

   Module des vues pour l'API et l'interface web des tâches.

   Ce module définit :
   Un **ViewSet API REST** basé sur Django REST Framework.
   Une **interface HTML** avec HTMX pour un CRUD dynamique.







Module Contents
---------------

.. py:class:: TaskViewSet(**kwargs)

   Bases: :py:obj:`rest_framework.viewsets.ModelViewSet`


   ViewSet pour gérer les tâches via l'API REST.

   Routes disponibles :
   - **GET /tasks/** : Liste toutes les tâches.
   - **POST /tasks/** : Crée une nouvelle tâche.
   - **GET /tasks/{id}/** : Récupère une tâche spécifique.
   - **PUT /tasks/{id}/** : Met à jour une tâche existante.
   - **DELETE /tasks/{id}/** : Supprime une tâche.


   .. py:attribute:: queryset


   .. py:attribute:: serializer_class


.. py:function:: home(request)

   Page d'accueil avec un menu de navigation.


.. py:function:: task_list(request)

   Affiche une page HTML avec toutes les tâches sous forme de liste.

   Cette vue retourne un rendu HTML et est utilisée avec HTMX pour
   un CRUD dynamique.


.. py:function:: task_create(request)

   Ajoute une nouvelle tâche avec HTMX.

   Cette vue renvoie un template HTML partiel contenant la tâche ajoutée.


.. py:function:: task_delete(request, task_id)

   Supprime une tâche et met à jour la liste, sans recréer le conteneur principal.


.. py:function:: task_update(request, task_id)

   Met à jour une tâche existante avec HTMX.

   - `GET` : Affiche le formulaire d'édition.
   - `POST` : Enregistre la modification et affiche la tâche mise à jour.


