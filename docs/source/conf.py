# Configuration file for the Sphinx documentation builder.

import os
import sys
import django

# Ajuste le chemin du projet Django pour Sphinx
sys.path.insert(0, os.path.abspath('../../'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'
django.setup()

# -- Informations du projet -----------------------------------------------------
project = 'Django-CI/CD'
copyright = '2025, TzRPheonix'
author = 'TzRPheonix'

# -- Extensions Sphinx activées ------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',        # Génération auto de doc depuis les docstrings
    'sphinx.ext.autosummary',     # Résumés automatiques pour chaque module/classe
    'sphinx.ext.napoleon',        # Support des docstrings Google/NumPy
    'sphinx.ext.viewcode',        # Ajoute des liens vers le code source
    'sphinx.ext.todo',            # Active les TODOs dans la documentation
    'sphinx.ext.intersphinx',     # Permet de créer des liens vers d'autres docs (Django/Python)
    'sphinx.ext.autodoc.typehints',  # Extraction des annotations de type Python
]

# Génération automatique des fichiers RST pour chaque module
autosummary_generate = True

# Options de génération automatique de la documentation
autodoc_default_options = {
    'members': True,          # Inclut les classes/fonctions/méthodes
    'undoc-members': True,    # Inclut même celles sans docstring
    'show-inheritance': True, # Affiche l'héritage des classes
    'no-index': True,         # ✅ Évite les erreurs de duplication
    'special-members': '__init__',  # Inclut les constructeurs
}

# -- Options pour Intersphinx --------------------------------------------------
# Téléchargement manuel des fichiers objects.inv pour une documentation locale
objects_inv_dir = os.path.abspath('')

intersphinx_mapping = {
    "python": (objects_inv_dir + "/python_objects", None),
    "django": (objects_inv_dir + "/django_objects", None),
}

# -- Chemins des templates -----------------------------------------------------
templates_path = ['_templates']
exclude_patterns = []

# -- Options de sortie HTML ----------------------------------------------------
html_theme = 'sphinx_rtd_theme'  # Thème ReadTheDocs
html_static_path = ['_static']

html_theme_options = {
    "navigation_depth": 4,  # Affiche plus de niveaux de navigation
    "collapse_navigation": False,  # Garde le menu toujours ouvert
    "sticky_navigation": True,  # Fixe la barre de navigation
}

# -- Options des TODOs ---------------------------------------------------------
todo_include_todos = True  # ✅ Affiche les TODOs dans la documentation

# -- Options pour les annotations de type et l'héritage ------------------------
autodoc_typehints = "description"  # ✅ Affiche les annotations de type
autodoc_inherit_docstrings = True  # ✅ Hérite des docstrings parent
