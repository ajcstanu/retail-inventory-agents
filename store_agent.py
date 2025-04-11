class StoreAgent:
    def __init__(self):
        self.stock = 50

    def forecast_demand(self, signal):
        return signal + 5

    def check_stock(self, forecast):
        return self.stock < forecast

    def create_restock_request(self):
        return {"item": "product", "quantity": 30}

    def update_inventory(self, incoming):
        self.stock += incoming["quantity"]
