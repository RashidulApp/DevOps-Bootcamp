class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append({"product": product, "quantity": quantity})

    def calculate_total(self):
        total = sum(item["product"].price * item["quantity"] for item in self.items)
        return total

class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.shopping_cart = ShoppingCart()

    def make_purchase(self):
        total_cost = self.shopping_cart.calculate_total()
        print(f"{self.name} made a purchase of ${total_cost}.")


# Create products
product1 = Product(1, "Laptop", 1200)
product2 = Product(2, "Headphones", 100)

# Create a customer
customer = Customer("C001", "Alice", "alice@email.com")

# Add items to the shopping cart
customer.shopping_cart.add_item(product1, 2)
customer.shopping_cart.add_item(product2, 1)

# Make a purchase
customer.make_purchase()
