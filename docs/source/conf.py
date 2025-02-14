# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Configuration du chemin du projet Django ----------------------------------
PROJECT_DIR = os.path.abspath('../../')  # Racine du projet
APP_DIR = os.path.join(PROJECT_DIR, 'myproject')  # Répertoire de l'application
CORE_DIR = os.path.join(PROJECT_DIR, 'core')  # Répertoire d'une app spécifique (si nécessaire)

sys.path.insert(0, PROJECT_DIR)
sys.path.insert(0, APP_DIR)
sys.path.insert(0, CORE_DIR)

# -- Configuration Django ------------------------------------------------------
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

try:
    import django
    django.setup()
except ModuleNotFoundError as e:
    print(f" Django n'a pas pu être configuré : {e}. Vérifie que l'environnement virtuel est activé.")

# -- Informations du projet -----------------------------------------------------
project = 'Django-CI/CD'
copyright = '2025, TzRPheonix'
author = 'TzRPheonix'

# -- Extensions Sphinx activées ------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',        # Génération auto de doc depuis les docstrings
    'sphinx.ext.napoleon',        # Support des docstrings Google/NumPy
    'sphinx.ext.viewcode',        # Ajoute des liens vers le code source
    'sphinx.ext.todo',            # Active les TODOs dans la documentation
    'sphinx.ext.intersphinx',     # Permet de créer des liens vers d'autres docs (Django/Python)
    'sphinx.ext.autodoc.typehints',  # Extraction des annotations de type Python
    'sphinx.ext.ifconfig',        # Permet des configurations conditionnelles
    'autoapi.extension',   # AutoAPI : Génération de documentation sans docstrings
]
# -- Configuration de AutoAPI --------------------------------------------------
autoapi_type = "python"  # Type d'analyse : Python
autoapi_dirs = ["../../myproject", "../../core"]  # Scanner automatiquement le code source
autoapi_add_toctree_entry = True  # Ajoute automatiquement la doc dans la navigation
autoapi_keep_files = True  # Garde les fichiers intermédiaires (utile pour debug)
autoapi_options = [
    "members",
    "undoc-members",  # Inclut les fonctions sans docstrings
    "show-inheritance",
    "special-members",
    "private-members",  # Inclut les méthodes privées (_test_function)
]


# -- Options pour Intersphinx --------------------------------------------------
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
}

# -- Chemins des templates -----------------------------------------------------
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options de sortie HTML ----------------------------------------------------
try:
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'  # Thème ReadTheDocs
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
except ImportError:
    html_theme = 'alabaster'  # Fallback si `sphinx_rtd_theme` n'est pas installé
    print("`sphinx_rtd_theme` n'est pas installé. Utilisation du thème 'alabaster'.")

html_theme_options = {
    "navigation_depth": 4,  # Affiche plus de niveaux de navigation
    "collapse_navigation": False,  # Garde le menu toujours ouvert
    "sticky_navigation": True,
}

# -- Options des TODOs ---------------------------------------------------------
todo_include_todos = True

# -- Affichage automatique des types d'arguments et de retour ----------------
autodoc_typehints = "description"  # Affiche les types des arguments et des valeurs de retour
autodoc_typehints_format = "short"  # Affiche `str`, `int` au lieu de `builtins.str`
autodoc_inherit_docstrings = True  # Récupère les docstrings des classes parentes
