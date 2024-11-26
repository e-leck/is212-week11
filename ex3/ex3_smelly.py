class Product:
    def __init__(self, name, price, discount_rate, tax_rate):
        self.name = name
        self.price = price
        self.discount_rate = discount_rate
        self.tax_rate = tax_rate

    def apply_discount(self):
        discounted_price = self.price - (1 * self.discount_rate)
        print(f"Discounted price for {self.name} (Grocery): {discounted_price}")
        return discounted_price
    
    def calculate_tax(self):
        tax = self.price * self.tax_rate
        print(f"Tax for {self.name} (Grocery): {tax}")
        return tax

class Electronics(Product):
    def __init__(self, name, price):
        super().__init__(name, price, discount_rate=0.10, tax_rate=0.15)

class Electronics(Product):
    def __init__(self, name, price):
        super().__init__(name, price, discount_rate=0.20, tax_rate=0.08)

class Electronics(Product):
    def __init__(self, name, price):
        super().__init__(name, price, discount_rate=0.05, tax_rate=0.02)
