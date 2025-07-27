Python 3.10.11 (v3.10.11:7d4cc5aa85, Apr  4 2023, 19:05:19) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>🌿 Ease - Smart Aggregator</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">

  <style>
    body {
      font-family: 'Poppins', sans-serif;
      background: linear-gradient(to right, #f0fff3, #e0f7fa);
      margin: 0;
      padding: 0;
    }

    #welcomePage {
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100vh;
      background: linear-gradient(135deg, #a8edea, #fed6e3);
    }

    .welcome-container {
      text-align: center;
      background: white;
      padding: 50px;
      border-radius: 25px;
      box-shadow: 0 10px 40px rgba(0,0,0,0.1);
      animation: fadeIn 1s ease-in-out;
    }

    .welcome-container h1 {
      font-size: 3rem;
      font-weight: bold;
      color: #1e5128;
    }

    .welcome-container p {
      font-size: 18px;
      color: #555;
      margin-top: 10px;
    }

    .welcome-container button {
      margin-top: 30px;
      padding: 12px 25px;
      font-size: 18px;
      border-radius: 10px;
      border: none;
      background-color: #198754;
      color: white;
      transition: background 0.3s ease;
    }

    .welcome-container button:hover {
      background-color: #157347;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: scale(0.9); }
      to { opacity: 1; transform: scale(1); }
    }

    #mainApp {
      display: none;
    }

    .section-title {
      font-size: 1.6rem;
      font-weight: 600;
      color: #198754;
      margin-bottom: 15px;
      border-left: 6px solid #198754;
      padding-left: 12px;
      background: #ecfdf5;
      border-radius: 5px;
    }

    #vendorResults p {
      background-color: #f8f9fa;
      padding: 15px;
      border-radius: 10px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.05);
    }

    #map {
      height: 400px;
      width: 100%;
      border-radius: 12px;
      margin-top: 10px;
    }

    #infoBox {
      font-size: 14px;
      color: #333;
      margin-top: 10px;
    }

    #loading {
      font-size: 16px;
      color: #777;
      margin-top: 5px;
    }
  </style>
</head>
<body>

  <!-- Welcome Page -->
  <div id="welcomePage">
    <div class="welcome-container">
      <h1>🌿 Welcome to Ease</h1>
      <p>Smart Bulk Order Aggregator for Farmers, Vendors & Suppliers</p>
      <button onclick="showMainApp()">Get Started</button>
    </div>
  </div>

  <!-- Main App -->
  <div id="mainApp">
    <nav class="navbar navbar-expand-lg navbar-dark bg-success">
      <div class="container-fluid">
        <a class="navbar-brand mx-auto fw-bold" href="#">🌾 Ease App Dashboard</a>
      </div>
    </nav>

    <div class="container py-4">
      <div class="card shadow-sm mb-4">
        <div class="card-body">
          <h2 class="section-title">🔍 Search for Item</h2>
          <div class="row g-3">
            <div class="col-md-6">
              <input type="text" id="searchItem" class="form-control" placeholder="Enter item name (e.g., tomato)">
            </div>
            <div class="col-md-6">
              <input type="text" id="searchLocation" class="form-control" placeholder="Enter your location (e.g., Chennai)">
            </div>
            <div class="col-12">
              <button onclick="searchVendors()" class="btn btn-success w-100">Search Nearest Vendors</button>
            </div>
          </div>
        </div>
      </div>

      <div class="card shadow-sm mb-4">
        <div class="card-body">
          <h2 class="section-title">📍 Nearest Vendors</h2>
          <div id="vendorResults">🔎 Search to view nearby vendors.</div>
        </div>
      </div>

      <div class="card shadow-sm">
        <div class="card-body">
          <h2 class="section-title">🗺 Your Live Location</h2>
          <div id="map"></div>
          <div id="infoBox">Fetching your location...</div>
          <div id="loading">🛰 Getting location...</div>
        </div>
      </div>
    </div>
  </div>

  <script>
    function showMainApp() {
      document.getElementById("welcomePage").style.display = "none";
      document.getElementById("mainApp").style.display = "block";
      initMap();
    }

    async function searchVendors() {
      const item = document.getElementById('searchItem').value;
      const location = document.getElementById('searchLocation').value;

      const res = await fetch(`http://localhost:5000/search?item=${item}&location=${location}`);
      const data = await res.json();

      let html = '';
      data.forEach(vendor => {
        html += `
          <p>
            👤 <b>${vendor.name}</b><br>
            📍 ${vendor.location}<br>
            🧺 ${vendor.material}<br>
            📦 Quantity: ${vendor.quantity}<br>
            ⏱ ETA: ${vendor.eta} min<br>
            <button onclick="placeOrder('${vendor.name}', '${vendor.material}')" class="btn btn-sm btn-outline-success mt-2">Order</button>
          </p>
        `;
      });

      document.getElementById('vendorResults').innerHTML = html || "<p class='text-danger'>❌ No vendors found nearby.</p>";
    }

    async function placeOrder(vendor, item) {
      const quantity = prompt(`Enter quantity to order from ${vendor} for ${item}:`);
      if (!quantity || isNaN(quantity)) return alert("Please enter a valid number.");

      const res = await fetch("http://localhost:5000/order", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          vendor,
          material: item,
          quantity: parseInt(quantity),
          location: "User Search"
        })
      });

      const result = await res.json();
      alert("✅ Order placed successfully!");
    }

    function getUserLocation(callback) {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
          position => {
            const coords = {
              lat: position.coords.latitude,
              lng: position.coords.longitude
            };
            callback(coords);
          },
          error => {
            document.getElementById("infoBox").innerText = "❌ Location access denied.";
            console.error(error);
          }
...         );
...       } else {
...         document.getElementById("infoBox").innerText = "❌ Geolocation not supported.";
...       }
...     }
... 
...     let map;
... 
...     function initMap() {
...       getUserLocation(coords => {
...         map = new google.maps.Map(document.getElementById("map"), {
...           center: coords,
...           zoom: 15
...         });
... 
...         new google.maps.Marker({
...           position: coords,
...           map: map,
...           title: "📍 You are here",
...           icon: 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png'
...         });
... 
...         document.getElementById("infoBox").innerText =
...           `Latitude: ${coords.lat.toFixed(5)}, Longitude: ${coords.lng.toFixed(5)}`;
... 
...         document.getElementById("loading").style.display = "none";
...       });
...     }
...   </script>
... 
...   <!-- ✅ Google Maps API Key Included -->
...   <script async defer
...     src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDnoR6Bs_x8F4oYKnKtdDWqTL-ixGZRFuA&callback=initMap">
...   </script>
... 
... </body>
