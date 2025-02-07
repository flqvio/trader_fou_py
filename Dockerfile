# Utiliser une image de base officielle Python
FROM python:3.13.1-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de dépendances
COPY requirements.txt requirements.txt

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste de l'application
COPY . .

# Exposer le port sur lequel l'application va tourner
EXPOSE 5000

# Commande pour exécuter l'application
CMD ["python", "app.py"]
