
# Crypto Price Tracker (CPT)

Crypto Price Tracker is a simple web application that allows users to track real-time prices of cryptocurrencies like Bitcoin and Ethereum. The project integrates Python (Flask) and Node.js for seamless backend and frontend functionality.

---

## Features

- **Real-time Cryptocurrency Prices**: Displays live prices for Bitcoin and Ethereum fetched from the CoinGecko API.
- **Responsive Design**: Uses Bootstrap for a modern and mobile-friendly user interface.
- **Python-Node.js Integration**: Combines the strengths of Python for data fetching and Node.js for frontend rendering.

---

## Requirements

### Python
- Python 3.8 or higher
- Flask
- Requests

### Node.js
- Node.js 14.x or higher
- npm (Node Package Manager)

---

## Setup Instructions

### Backend (Python)
1. Clone the repository:
    ```bash
    git clone https://github.com/infalibless/crypto-price-tracker.git
    cd crypto-price-tracker
    ```
2. Navigate to the Python backend folder and install dependencies:
    ```bash
    cd backend
    pip install flask requests
    ```
3. Start the Python server:
    ```bash
    python api.py
    ```

### Frontend (Node.js)
1. Navigate to the Node.js frontend folder and install dependencies:
    ```bash
    cd ../frontend
    npm install
    ```
2. Start the Node.js web+:
    ```bash
    node web.js
    ```

---

## Usage
1. Start the Python backend and Node.js frontend as described above.
2. Open your web browser and navigate to `http://localhost:3000`.
3. View live cryptocurrency prices for Bitcoin and Ethereum.

---

## Future Enhancements
- Add more cryptocurrencies.
- Implement user authentication for personalized watchlists.
- Integrate historical price data with graphs.

---

## Acknowledgements
- [CoinGecko API](https://www.coingecko.com/en/api) for cryptocurrency price data.
- Bootstrap for frontend styling.

---
