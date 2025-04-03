from collections import deque

class coffeeShop:
    def __init__(self):
        self.queue = deque()

    def takeOrder(self, name, order):
        ##Take a new order from a customer.
        name = input("Please enter your name: ")
        print(f"Hello {name}, welcome to the Coffee Shop!")
        print("Menu:")
        print("1. Black Coffee")
        print("2. Latte")
        print("3. Cappuccino")
        print("4. Espresso")
        print("5. Mocha")
        print("6. Americano")
        print("7. Macchiato")
        
        try:
            order = int(input("Please enter your order (1-7): "))
            if order < 1 or order > 7:
                print("Invalid menu option. Please choose a number between 1 and 7.")
                return
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")
            return

        if not name:
            print("Name cannot be empty!")
            return

        if any(customer['name'] == name for customer in self.queue):
            print(f"{name}, you already have an order in the queue.")
            return

        menuItems = {
            1: "Black Coffee",
            2: "Latte",
            3: "Cappuccino",
            4: "Espresso",
            5: "Mocha",
            6: "Americano",
            7: "Macchiato"
        }
        orderName = menuItems[order]
        self.queue.append({"name": name, "order": orderName})
        print(f"Order received: {orderName} for {name}")

    def serveCustomer(self):
        if self.queue:
            customer = self.queue.popleft()
            print(f"Serving {customer['order']} to {customer['name']}")
        else:
            print("No customers in the queue!")

    def showQueue(self):
        if self.queue:
            print("Current queue:")
            for customer in self.queue:
                print(f"{customer['name']} - {customer['order']}")
        else:
            print("The queue is empty!")

# Main function to run the Coffee Shop simulation
shop = coffeeShop()
while True:
    print("\nWelcome to Ryan's Coffee Shop!")
    print("1. Take Order")
    print("2. Serve Customer")
    print("3. Show Queue")
    print("4. Exit")
    choice = input("Please choose an option: ")

    if choice == "1":
        shop.takeOrder("", "")
    elif choice == "2":
        shop.serveCustomer()
    elif choice == "3":
        shop.showQueue()
    elif choice == "4":
        print("Thank you for visiting the Coffee Shop!")
        break
    else:
        print("Invalid choice. Please try again.")
