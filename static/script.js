async function getPrice() {
    const crypto = document.getElementById('crypto-select').value;
    const response = await fetch('/get_crypto_price', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `crypto=${crypto}`
    });
    const data = await response.json();
    const price = data[crypto];
    document.getElementById('price-display').innerText = `Price of ${crypto}: $${price}`;
}

async function addFavorite() {
    const crypto = document.getElementById('crypto-select').value;
    const response = await fetch('/add_favorite', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `crypto=${crypto}`
    });
    const data = await response.json();
    updateFavorites(data.favorites);
}

async function updateFavorites(favorites) {
    const favoritesList = document.getElementById('favorites-list');
    favoritesList.innerHTML = '';
    for (const crypto of favorites) {
        const response = await fetch('/get_crypto_price', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `crypto=${crypto}`
        });
        const data = await response.json();
        const price = data[crypto];
        const li = document.createElement('li');
        li.innerText = `${crypto}: $${price}`;
        favoritesList.appendChild(li);
    }
}

async function loadFavorites() {
    const response = await fetch('/get_favorites');
    const data = await response.json();
    updateFavorites(data.favorites);
}

loadFavorites();
