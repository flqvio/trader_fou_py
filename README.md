# CryptoTracker

Une application web moderne pour suivre les prix des cryptomonnaies en temps réel.

## Fonctionnalités

1. **Liste des Cryptomonnaies**
   - Affichage des top 50 cryptomonnaies
   - Prix en temps réel
   - Variation sur 24h
   - Market Cap

2. **Recherche**
   - Filtrage en temps réel des cryptomonnaies
   - Recherche par nom ou symbole

3. **Graphiques Détaillés**
   - Visualisation de l'évolution des prix sur 7 jours
   - Interface interactive avec tooltips
   - Mode plein écran pour les détails

## Prérequis

- Node.js 20.x ou supérieur
- npm 9.x ou supérieur
- Docker (pour le déploiement)

## Installation

```bash
# Cloner le repository
git clone https://github.com/votre-username/cryptotracker.git
cd cryptotracker

# Installer les dépendances
npm install

# Démarrer en mode développement
npm run dev
```

## Tests

```bash
# Lancer les tests
npm run test

# Lancer les tests avec couverture
npm run test:coverage
```

## Build & Déploiement

### Build Local

```bash
npm run build
```

### Docker

```bash
# Build de l'image
docker build -t cryptotracker .

# Lancement du container
docker run -p 80:80 -e VITE_COINGECKO_API_KEY=votre_api_key cryptotracker
```

## CI/CD

Le projet utilise GitHub Actions pour l'intégration et le déploiement continus.

### Workflow

1. **Pull Requests**
   - Tests automatiques
   - Vérification du linting
   - Review obligatoire avant merge

2. **Main Branch**
   - Tests
   - Build de l'image Docker
   - Push sur Docker Hub avec le SHA du commit

3. **Releases**
   - Tests
   - Build de l'image Docker
   - Push sur Docker Hub avec le tag de la release

## Variables d'Environnement

- `VITE_COINGECKO_API_KEY`: Clé API CoinGecko (optionnelle pour le développement)

## Architecture

- React + TypeScript pour le frontend
- Vite comme bundler
- Tailwind CSS pour le styling
- Chart.js pour les graphiques
- Testing Library + Vitest pour les tests

## Contribution

1. Fork le projet
2. Créer une branche pour votre feature (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push sur la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## License

MIT