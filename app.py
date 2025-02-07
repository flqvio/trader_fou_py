from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# URL de l'API Gemini pour récupérer les symboles
GEMINI_SYMBOLS_URL = "https://api.gemini.com/v1/symbols"

# Récupérer la liste des symboles disponibles
response = requests.get(GEMINI_SYMBOLS_URL)
symbols = response.json()

# Liste des favoris, initialisée globalement
favorites = []

@app.route('/')
def index():
    return render_template('index.html', symbols=symbols)

@app.route('/get_crypto_price', methods=['POST'])
def get_crypto_price():
    crypto_id = request.form.get('crypto')
    # Utiliser l'API Gemini pour obtenir le prix
    response = requests.get(f"https://api.gemini.com/v1/pubticker/{crypto_id}")
    data = response.json()
    price = data.get('last', 'N/A')
    return jsonify({crypto_id: price})

@app.route('/add_favorite', methods=['POST'])
def add_favorite():
    global favorites  # Utiliser la variable globale
    crypto_id = request.form.get('crypto')
    if crypto_id not in favorites:
        favorites.append(crypto_id)
    return jsonify({"favorites": favorites})

@app.route('/get_favorites', methods=['GET'])
def get_favorites():
    global favorites  # Utiliser la variable globale
    return jsonify({"favorites": favorites})

if __name__ == '__main__':
    app.run(debug=True)
