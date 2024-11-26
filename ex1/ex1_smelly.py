class OrderProcessor:
    def process_order(self, order):
        # Step 1: Validate order details
        self.validate_order(order)

        # Step 2: Calculate total price
        total_price = self.calculate_price(order)

        # Step 3: Apply discounts if applicable
        total_price = total_price * self.get_discount_rate(order)

        # Step 4: Update inventory
        self.update_inventory(order)

        # Step 5: Generate receipt
        receipt = self.generate_receipt(order, total_price)

         # Step 6: Send confirmation email
        self.send_email(order, receipt)

        return receipt

    def validate_order(self, order):
        if not (order.get("customer_id")):
            raise ValueError("Customer ID is required.")
        if not (order.get("items")):
            raise ValueError("Order must contain items.")
        
    def get_discount_rate(self, order):
        discount_rate = 1
        if (order.get("discount_code")) == "SUMMER20":
            discount_rate = 0.8  # 20% discount
        elif (order.get("discount_code")) == "WELCOME10":
            discount_rate = 0.9  # 10% discount
        return discount_rate
        
    def calculate_price(self, order):
        items = order.get("items")
        total_price = 0
        for item in items:
            total_price += item["price"] * item["quantity"]
        return total_price

    def update_inventory(self, order):
        items = order.get("items")
        for item in items:
            item_id = item["id"]
            quantity = item["quantity"]
            # Code to update inventory for each item
            # (for simplicity, let's assume a simple print statement here)
            print(f"Updating inventory for item {item_id}, reducing stock by {quantity}.")

    def generate_receipt(self, order, total_price):
        items = order.get("items")
        receipt = f"Customer ID: {order.get("customer_id")}\n"
        receipt += "Items:\n"
        for item in items:
            receipt += f"- {item['name']}: {item['quantity']} x ${item['price']}\n"
        receipt += f"Total: ${total_price:.2f}\n"
        return receipt

    def send_email(self, order, receipt):
        print(f"Sending email to customer {order.get("customer_id")} with receipt:\n{receipt}")
    
            