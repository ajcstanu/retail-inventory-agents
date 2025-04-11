class SupplierAgent:
    def fulfill_order(self, request):
        return {"stock": request["quantity"]}
