from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
import os

from agents.store_agent import StoreAgent
from agents.customer_agent import CustomerAgent
from agents.warehouse_agent import WarehouseAgent
from agents.supplier_agent import SupplierAgent

app = Flask(__name__, static_folder="frontend", static_url_path="")
CORS(app)

@app.route("/")
def serve_index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/script.js")
def serve_script():
    return send_from_directory(app.static_folder, "script.js")

@app.route("/styles.css")
def serve_styles():
    return send_from_directory(app.static_folder, "styles.css")

@app.route("/simulate")
def simulate():
    customer = CustomerAgent()
    store = StoreAgent()
    warehouse = WarehouseAgent()
    supplier = SupplierAgent()

    demand = customer.generate_demand_signal()
    forecast = store.forecast_demand(demand)
    low_stock = store.check_stock(forecast)

    if low_stock:
        request = store.create_restock_request()
        response = warehouse.handle_restock_request(request)
        if not response['fulfilled']:
            supply = supplier.fulfill_order(request)
            warehouse.receive_stock(supply['stock'])
        dispatched = warehouse.dispatch_stock(request)
        store.update_inventory(dispatched)

    return jsonify({
        "Customer Demand": demand,
        "Forecasted Demand": forecast,
        "Store Stock": store.stock,
        "Warehouse Stock": warehouse.stock
    })

if __name__ == '__main__':
    if not os.path.exists("frontend/index.html"):
        raise FileNotFoundError("index.html not found in 'frontend' folder.")
    app.run(debug=True, port=8000)
