import uuid

# MenuItem class
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Order class
class Order:
    def __init__(self, customer_name):
        self.order_id = uuid.uuid4()  # Unique order ID
        self.customer_name = customer_name
        self.items = []
        self.total = 0

    def add_item(self, item, quantity):
        self.items.append((item, quantity))
        self.total += item.price * quantity
        print(f"Added {quantity} x {item.name} → Current Total: ₹{self.total}")

    def show_bill(self):
        print("\n========== Final Bill ==========")
        print(f"Order ID: {self.order_id}")
        print(f"Customer: {self.customer_name}")
        for item, quantity in self.items:
            print(f"{item.name} x {quantity} = ₹{item.price * quantity}")
        print(f"Total Bill: ₹{self.total}")
        print("================================\n")

# Cafe class
class Cafe:
    def __init__(self):
        self.menu = [
            MenuItem("Espresso", 50),
            MenuItem("Latte", 70),
            MenuItem("Cappuccino", 80),
            MenuItem("Americano", 60),
            MenuItem("Mocha", 90)
        ]

    def show_menu(self):
        print("\n---- Cafe Menu ----")
        for item in self.menu:
            print(f"{item.name} - ₹{item.price}")

    def get_item(self, name):
        for item in self.menu:
            if item.name.lower() == name.strip().lower():
                return item
        return None

# Main Program
cafe = Cafe()
cust_name = input("Enter your name: ").strip() or "Guest"
order = Order(cust_name)

while True:
    cafe.show_menu()
    choice = input("Enter coffee names to order (comma separated, or 'done' to finish): ")
    if choice.lower() == "done":
        break

    coffee_names = choice.split(",")  # Split multiple coffee names
    for coffee_name in coffee_names:
        item = cafe.get_item(coffee_name)
        if item:
            while True:
                try:
                    qty = int(input(f"Enter quantity of {item.name}: "))
                    if qty <= 0:
                        print("Quantity must be positive.")
                        continue
                    break
                except ValueError:
                    print("Invalid number. Please enter again.")
            order.add_item(item, qty)
        else:
            print(f"❌ '{coffee_name.strip()}' not found in menu.")

# Show final bill
order.show_bill( )