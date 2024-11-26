from flask import Flask, jsonify
import requests

app = Flask(__name__)

def get_crypto_prices():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum",
        "vs_currencies": "usd"
    }
    response = requests.get(url, params=params)
    return response.json()

@app.route('/prices', methods=['GET'])
def prices():
    data = get_crypto_prices()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
