products = {}
daily_revenue = 0




def add_item():
    print("\n--- ADD A NEW ITEM ---")

    name = input("Item name: ").strip().title()

    if not name or name in products:
        print("Invalid name or item already exists!")
        return

    try:
        stock = int(input("Current stock quantity: "))
        selling_price = float(input("Selling price per unit (TL): "))
        purchase_price = float(input("Purchase cost per unit (TL): "))
        limit = int(input("Low-stock warning limit: "))
        target = int(input("Target stock quantity: "))

        if stock < 0 or selling_price < 0 or purchase_price < 0 or limit < 0:
            print("Negative values are not allowed!")
            return

        if target < stock:
            print("Target stock cannot be lower than current stock!")
            return

        products[name] = {
            "stock": stock,
            "selling_price": selling_price,
            "purchase_price": purchase_price,
            "limit": limit,
            "target": target }

        print(f"{name} added successfully!")

    except ValueError:
        print("Invalid input! Please enter numeric values.")


def sell_items():
    global daily_revenue

    if not products:
        print("Please add an item first!")
        return

    print("\n--- SELL AN ITEM ---")

    for name, product in products.items():
        print(f"{name} | Stock: {product['stock']} units")

    name = input("Item name: ").strip().title()

    if name not in products:
        print("Item not found!")
        return

    try:
        quantity = int(input("Quantity sold: "))

        if quantity <= 0:
            print("Quantity must be at least 1!")
            return

        product = products[name]

        if quantity > product["stock"]:
            print(f"Insufficient stock! Available: {product['stock']}")
            return

        revenue = quantity * product["selling_price"]
        product["stock"] -= quantity
        daily_revenue += revenue

        print("\nSALE COMPLETED!")
        print(f"Product: {name}")
        print(f"Sale revenue: {revenue:.2f} TL")
        print(f"Remaining stock: {product['stock']} units")

        if product["stock"] <= product["limit"]:
            print("WARNING: Stock level is low!")

    except ValueError:
        print("Please enter a valid quantity!")


def restock_item():
    if not products:
        print("Please add an item first!")
        return

    print("\n--- RESTOCK AN ITEM ---")

    for name, product in products.items():
        print(f"{name} | Current stock: {product['stock']} units")

    name = input("Item name to restock: ").strip().title()

    if name not in products:
        print("Item not found!")
        return

    try:
        quantity = int(input("Quantity purchased: "))

        if quantity <= 0:
            print("Quantity must be at least 1!")
            return

        product = products[name]
        cost = quantity * product["purchase_price"]

        product["stock"] += quantity

        print("\nSTOCK UPDATED SUCCESSFULLY!")
        print(f"Product: {name}")
        print(f"Quantity added: {quantity} units")
        print(f"New stock level: {product['stock']} units")
        print(f"Purchase cost: {cost:.2f} TL")

        if product["stock"] <= product["limit"]:
            print("WARNING: Stock is still low!")
        else:
            print("Stock level is sufficient.")

    except ValueError:
        print("Please enter a valid quantity!")


def show_reports():
    print("\n--- DAILY REPORT ---")
    print(f"Total daily revenue: {daily_revenue:.2f} TL")

    if not products:
        print("No items registered.")
        return

    total_restock_cost = 0

    print("\n--- STOCK AND RESTOCKING REPORT ---")

    for name, product in products.items():
        needed = max(0, product["target"] - product["stock"])
        cost = needed * product["purchase_price"]
        total_restock_cost += cost

        print(f"\nProduct: {name}")
        print(f"Current stock: {product['stock']} units")

        if product["stock"] <= product["limit"]:
            print("Status: LOW STOCK WARNING!")
        else:
            print("Status: Normal")

        print(f"Quantity to order: {needed} units")
        print(f"Purchase price per unit: {product['purchase_price']:.2f} TL")
        print(f"Restocking cost: {cost:.2f} TL")

    print(f"\nTotal restocking cost: {total_restock_cost:.2f} TL")


while True:
    print("\n" + "=" * 44)
    print("    STOKITO - SMART STOCK ASSISTANT")
    print("=" * 44)
    print("1 - Add a new item")
    print("2 - Sell an item")
    print("3 - View daily revenue and stock reports")
    print("4 - List all registered items")
    print("5 - Restock an existing item")
    print("0 - Exit")
    print("=" * 44)

    choice = input("\nWhat would you like to do? ").strip()

    if choice == "1":
        add_item()
    elif choice == "2":
        sell_items()
    elif choice == "3":
        show_reports()
    elif choice == "4":
        if not products:
            print("No items registered yet.")
        else:
            print("\n---- REGISTERED  ITEMS ----")
            for name, product in products.items():
                print(
                    f"{name} | Stock: {product['stock']} units |  "
                    f"Selling price: {product['selling_price']:.2f} TL"
                )
    elif choice == "5":
        restock_item()
    elif choice == "0":
        print(" Thank you for using Stokito !!")
        break
    else:
        print("Invalid choice!!!! Please select an option from 0 to 5.")