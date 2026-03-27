# Main Application Module
# Controls the program flow and user interaction
from file_manager import load_csv, save_csv
from services import (
    add_product,
    show_inventory,
    find_product,
    update_product,
    delete_product,
    calculate_statistics
)

# In-memory inventory storage
inventory = []

# Control variable for loop execution
running = True

# ── MAIN MENU LOOP ─────────────────────────────────────────────
while running:
    print("""
     INVENTORY MENU
    -------------------------
    1. Add product
    2. Show inventory
    3. Search product
    4. Update product
    5. Delete product
    6. Statistics
    7. Save CSV
    8. Load CSV
    9. Exit
    -------------------------
    """)

    option = input("Option: ").strip()

    try:
        # Option 1: Add product
        if option == "1":
            name = input("Name: ").strip()
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))

            if price < 0 or quantity < 0:
                print(" Values must be non-negative.")
                continue

            add_product(inventory, name, price, quantity)

        # Option 2: Show inventory
        elif option == "2":
            show_inventory(inventory)

        # Option 3: Search product
        elif option == "3":
            name = input("Search name: ").strip()
            product = find_product(inventory, name)

            if product:
                print(product)
            else:
                print(" Product not found.")

        # Option 4: Update product
        elif option == "4":
            name = input("Product name: ").strip()
            price = float(input("New price: "))
            quantity = int(input("New quantity: "))

            if update_product(inventory, name, price, quantity):
                print("Product updated.")
            else:
                print(" Product not found.")

        # Option 5: Delete product
        elif option == "5":
            name = input("Product name: ").strip()

            if delete_product(inventory, name):
                print(" Product deleted.")
            else:
                print(" Product not found.")

        # Option 6: Statistics
        elif option == "6":
            stats = calculate_statistics(inventory)

            if stats:
                print("\n STATISTICS")
                print(f"Total units: {stats['total_units']}")
                print(f"Total value: ${stats['total_value']:.2f}")
                print(f"Most expensive: {stats['most_expensive']}")
                print(f"Highest stock: {stats['highest_stock']}")
            else:
                print("📭 Inventory is empty.")

        # Option 7: Save CSV
        elif option == "7":
            path = input("File path: ")
            save_csv(inventory, path)

        # Option 8: Load CSV
        elif option == "8":
            path = input("File path: ")
            new_data = load_csv(path)

            if new_data:
                decision = input("Overwrite inventory? (Y/N): ").upper()

                if decision == "Y":
                    inventory = new_data
                    print(" Inventory replaced.")
                else:
                    # Merge policy
                    for p in new_data:
                        existing = find_product(inventory, p["name"])
                        if existing:
                            existing["quantity"] += p["quantity"]
                            existing["price"] = p["price"]
                        else:
                            inventory.append(p)

                    print(" Inventory merged.")

        # Option 9: Exit program
        elif option == "9":
            print(" Goodbye.")
            running = False

        else:
            print(" Invalid option.")

    except ValueError:
        print(" Invalid input. Use numeric values.")