const express = require('express');
const axios = require('axios');
const app = express();
const PORT = 3000;

app.use(express.static('public'));

app.get('/prices', async (req, res) => {
    try {
        const response = await axios.get('http://localhost:5000/prices');
        res.json(response.data);
    } catch (error) {
        console.error(error);
        res.status(500).send('err fetching prices');
    }
});

app.listen(PORT, () => {
    console.log(`-> http://localhost:${PORT}`);
});
