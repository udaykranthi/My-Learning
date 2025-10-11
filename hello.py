

class FoodApp:
    def __init__(self):
        self.menu = {
            1: {"name": "Pizza", "price": 250},
            2: {"name": "Burger", "price": 150},
            3: {"name": "Pasta", "price": 200},
            4: {"name": "Sandwich", "price": 120},
            5: {"name": "Coffee", "price": 80}
        }
        self.cart = {}
        self.order_placed = False

    def show_menu(self):
        print("\n------ MENU ------")
        for item_id, item in self.menu.items():
            print(f"{item_id}. {item['name']} - ₹{item['price']}")
        print("------------------")

    def add_to_cart(self):
        self.show_menu()
        try:
            item_id = int(input("Enter the item number to add: "))
            if item_id in self.menu:
                quantity = int(input("Enter quantity: "))
                if item_id in self.cart:
                    self.cart[item_id]['quantity'] += quantity
                else:
                    self.cart[item_id] = {
                        "name": self.menu[item_id]["name"],
                        "price": self.menu[item_id]["price"],
                        "quantity": quantity
                    }
                print(f"✅ {quantity} {self.menu[item_id]['name']}(s) added to cart.")
            else:
                print("❌ Invalid item number.")
        except ValueError:
            print("❌ Please enter valid numbers only.")

    def view_cart(self):
        if not self.cart:
            print("\n🛒 Cart is empty.")
            return
        print("\n------ YOUR CART ------")
        total = 0
        for item in self.cart.values():
            cost = item['price'] * item['quantity']
            total += cost
            print(f"{item['name']} x{item['quantity']} - ₹{cost}")
        print(f"------------------------\nTotal: ₹{total}")
        print("------------------------")

    def remove_from_cart(self):
        if not self.cart:
            print("Cart is empty, nothing to remove.")
            return
        self.view_cart()
        try:
            item_name = input("Enter the name of the item to remove: ").title()
            for item_id, item in list(self.cart.items()):
                if item['name'] == item_name:
                    del self.cart[item_id]
                    print(f"✅ {item_name} removed from cart.")
                    return
            print("❌ Item not found in cart.")
        except Exception as e:
            print("❌ Error:", e)

    def place_order(self):
        if not self.cart:
            print("❌ Your cart is empty. Add items first.")
            return
        self.view_cart()
        confirm = input("Do you want to place the order? (y/n): ").lower()
        if confirm == 'y':
            self.order_placed = True
            print("🛍️ Order placed successfully!")
        else:
            print("❌ Order not placed.")

    def cancel_order(self):
        if not self.order_placed:
            print("❌ No order to cancel.")
        else:
            confirm = input("Are you sure you want to cancel the order? (y/n): ").lower()
            if confirm == 'y':
                self.order_placed = False
                self.cart.clear()
                print("❌ Order cancelled successfully.")
            else:
                print("Order not cancelled.")

    def make_payment(self):
        if not self.order_placed:
            print("❌ No active order to pay for.")
            return
        total = sum(item['price'] * item['quantity'] for item in self.cart.values())
        print(f"\n💰 Total amount to pay: ₹{total}")
        payment_method = input("Enter payment method (Card/UPI/Cash): ").title()
        print(f"✅ Payment of ₹{total} done successfully using {payment_method}.")
        self.cart.clear()
        self.order_placed = False


def main():
    app = FoodApp()

    while True:
        print("""
        ====== FOOD APP MENU ======
        1. View Menu
        2. Add Item to Cart
        3. View Cart
        4. Remove Item from Cart
        5. Place Order
        6. Cancel Order
        7. Make Payment
        8. Exit
        ===========================
        """)
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            app.show_menu()
        elif choice == '2':
            app.add_to_cart()
        elif choice == '3':
            app.view_cart()
        elif choice == '4':
            app.remove_from_cart()
        elif choice == '5':
            app.place_order()
        elif choice == '6':
            app.cancel_order()
        elif choice == '7':
            app.make_payment()
        elif choice == '8':
            print("👋 Thank you for using the Food App! Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select between 1 and 8.")


if __name__ == "__main__":
    main()
