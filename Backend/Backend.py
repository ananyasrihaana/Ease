Python 3.10.11 (v3.10.11:7d4cc5aa85, Apr  4 2023, 19:05:19) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> const express = require('express');
... const cors = require('cors');
... const app = express();
... const PORT = 5000;
... 
... app.use(cors());
... app.use(express.json());
... 
... const vendors = [
...   { name: "Ravi's Farm", location: "Chennai", material: "tomato", quantity: 100, eta: 15 },
...   { name: "FreshCo Market", location: "Chennai", material: "onion", quantity: 200, eta: 10 },
...   { name: "Farm Basket", location: "Chennai", material: "tomato", quantity: 150, eta: 8 },
...   { name: "Harvest Supply", location: "Bangalore", material: "potato", quantity: 90, eta: 20 }
... ];
... 
... // Search Route
... app.get('/search', (req, res) => {
...   const { item, location } = req.query;
...   const results = vendors.filter(v =>
...     v.material.toLowerCase().includes(item.toLowerCase()) &&
...     v.location.toLowerCase().includes(location.toLowerCase())
...   );
...   res.json(results);
... });
... 
... // Order Route
... app.post('/order', (req, res) => {
...   console.log("✅ Order Received:", req.body);
...   res.json({ status: "success", message: "Order placed" });
... });
... 
... app.listen(PORT, () => {
...   console.log(`✅ Server running at http://localhost:${PORT}`);
