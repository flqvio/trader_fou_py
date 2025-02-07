import unittest
from app import app, favorites
import subprocess

class CryptoTrackerTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_get_crypto_price(self):
        result = self.app.post('/get_crypto_price', data={'crypto': 'btcusd'})
        self.assertEqual(result.status_code, 200)
        self.assertIn('btcusd', result.json)

    def test_add_favorite(self):
        global favorites  # Accéder à la variable globale
        favorites.clear()  # Réinitialiser les favoris pour le test
        result = self.app.post('/add_favorite', data={'crypto': 'btcusd'})
        self.assertEqual(result.status_code, 200)
        self.assertIn('btcusd', result.json['favorites'])

    def test_get_favorites(self):
        global favorites  # Accéder à la variable globale
        favorites.append('btcusd')  # Ajouter un favori pour le test
        result = self.app.get('/get_favorites')
        self.assertEqual(result.status_code, 200)
        self.assertIn('btcusd', result.json['favorites'])

    def test_add_duplicate_favorite(self):
        global favorites  # Accéder à la variable globale
        favorites.clear()  # Réinitialiser les favoris pour le test
        self.app.post('/add_favorite', data={'crypto': 'btcusd'})
        result = self.app.post('/add_favorite', data={'crypto': 'btcusd'})
        self.assertEqual(result.status_code, 404)
        self.assertEqual(favorites.count('btcusd'), 1)

if __name__ == '__main__':
    unittest.main()
