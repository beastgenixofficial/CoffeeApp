menu = {
    1: ("Espresso", 80),
    2: ("Cappuccino", 120),
    3: ("Latte", 140),
    4: ("Mocha", 160),
    5: ("Cold Coffee", 150)
}

cart = {}

def clear():
    print("\n" * 40)

while True:
    clear()

    print("=" * 35)
    print("      ☕ Beast ki Saxy Dukan ☕")
    print("=" * 35)

    print("\nMENU")
    for num, (name, price) in menu.items():
        print(f"{num}. {name:<15} ₹{price}")

    print("\n-------------------------")
    print("1. Order Item")
    print("2. View Cart")
    print("3. Checkout")
    print("4. Exit")
    print("-------------------------")

    choice = input("Choose an option: ")

    # ORDER ITEM
    if choice == "1":
        item_no = int(input("\nEnter coffee number: "))

        if item_no in menu:
            qty = int(input("Enter quantity: "))

            item_name = menu[item_no][0]
            cart[item_name] = cart.get(item_name, 0) + qty

            print(f"\n✓ {qty} {item_name}(s) added to cart.")
        else:
            print("\n❌ Invalid coffee number.")

        input("\nPress Enter to continue...")

    # VIEW CART
    elif choice == "2":
        clear()

        print("🛒 YOUR CART")
        print("-" * 25)

        if not cart:
            print("Cart is empty.")
        else:
            total = 0

            for item, qty in cart.items():
                for name, price in menu.values():
                    if name == item:
                        subtotal = price * qty
                        total += subtotal
                        print(f"{item:<15} x {qty} = ₹{subtotal}")

            print("-" * 25)
            print(f"Total = ₹{total}")

        input("\nPress Enter to return...")

    # CHECKOUT
    elif choice == "3":
        clear()

        if not cart:
            print("🛒 Cart is empty.")
            input("\nPress Enter to continue...")
            continue

        total = 0

        print("===== RECEIPT =====")

        for item, qty in cart.items():
            for name, price in menu.values():
                if name == item:
                    subtotal = price * qty
                    total += subtotal
                    print(f"{item:<15} x {qty} = ₹{subtotal}")

        print("-" * 25)
        print(f"Grand Total = ₹{total}")

        print("\n☕ Thank you for visiting Beast ki Saxy Dukan!")
        break

    # EXIT
    elif choice == "4":
        print("\n👋 Goodbye!")
        break

    else:
        print("\n❌ Invalid option.")
        input("\nPress Enter to continue...")