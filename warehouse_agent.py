class WarehouseAgent:
    def __init__(self):
        self.stock = 20

    def handle_restock_request(self, request):
        if self.stock >= request["quantity"]:
            self.stock -= request["quantity"]
            return {"fulfilled": True}
        return {"fulfilled": False}

    def receive_stock(self, quantity):
        self.stock += quantity

    def dispatch_stock(self, request):
        quantity = min(request["quantity"], self.stock)
        self.stock -= quantity
        return {"quantity": quantity}
