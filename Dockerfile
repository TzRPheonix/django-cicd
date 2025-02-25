# Utiliser une image Python optimisée
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier et installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Installer Gunicorn pour un meilleur serveur de production
RUN pip install gunicorn

# Copier tout le projet
COPY . .

# Exposer le port Django
EXPOSE 8000

# Commande pour gérer les migrations et lancer le serveur
CMD ["sh", "-c", "python manage.py migrate && gunicorn myproject.wsgi:application --bind 0.0.0.0:8000 --workers 4"]
