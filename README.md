### Documentation de trader_fou_py

## Qu'est-ce que c'est ?

**trader_fou_py** est une application web développée avec **Flask** qui permet aux utilisateurs de suivre les prix des cryptomonnaies et de gérer une liste de cryptomonnaies favorites. L'application interagit avec l'API Gemini pour récupérer les prix des cryptomonnaies en temps réel.

## Services / Fonctionnalités

- 💱 **Suivi des Prix des Cryptomonnaies** : Récupère et affiche les prix actuels des cryptomonnaies sélectionnées.
- ⭐ **Gestion des Favoris** : Ajoute et consulte une liste de cryptomonnaies favorites pour un accès rapide.
- 🌐 **Données en Temps Réel** : Utilise l'API Gemini pour garantir des informations à jour sur les cryptomonnaies.

---

## Voici  un aperçu de l'application

![Page d'Accueil](https://github.com/flqvio/trader_fou_py/tree/main/images/appli.png)

## Comment Construire

### Prérequis

- **Python** 3.13
- **pip** (gestionnaire de paquets Python)
- **Docker** (optionnel pour le déploiement en conteneur)

### Installation

```sh
git clone https://github.com/flqvio/trader_fou_py.git
cd trader_fou_py
pip install -r requirements.txt
```

### Processus de Construction

Pour une version prête à l'emploi, assurez-vous que toutes les dépendances sont installées et que l'application est correctement configurée.

---

## Comment Tester

### Exécution des Tests Unitaires

`trader_fou_py` utilise **unittest** pour tester les fonctionnalités de l'application.

```sh
python -m unittest discover -s tests
```

Cette commande exécutera tous les tests définis dans la suite de tests.

### Exemples de Fichiers de Test

- `test_app.py` : Contient des tests pour les principales fonctionnalités de l'application, y compris la récupération des prix et la gestion des favoris.

---

## Comment Exécuter Localement

Pour exécuter `trader_fou_py` en mode développement :

```sh
python app.py
```

Cela lancera le serveur de développement sur `http://127.0.0.1:5000/`.

---

## Comment Exécuter avec Docker

### Construction de l'Image Docker

```sh
docker build -t trader_fou_py .
```

### Exécution du Conteneur

```sh
docker run -p 5000:5000 trader_fou_py
```

L'application sera accessible à l'adresse `http://localhost:5000/`.

---

## CI/CD avec GitHub Actions

- **Pull Request** : Les tests sont exécutés à chaque push sur une pull request. La fusion est bloquée si les tests échouent ou si le code n'est pas revu.
- **Fusion vers le Trunk** : Les tests sont exécutés, l'application est construite, et l'image Docker est poussée avec le SHA du commit.
- **Release** : Les tests sont exécutés, l'application est construite, et l'image Docker est poussée avec le nom de la release.

---

Ce README fournit un guide complet pour comprendre, construire, tester et exécuter l'application web `trader_fou_py`. Si vous avez des questions ou besoin d'une assistance supplémentaire, n'hésitez pas à nous contacter !