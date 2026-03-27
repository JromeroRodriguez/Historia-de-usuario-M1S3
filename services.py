# Services Module
# Contains business logic (CRUD operations and statistics)


def find_product(inventory, name):
    """
    Search for a product by name (case insensitive).

    Returns:
        dict | None
    """
    for product in inventory:
        if product["name"].lower() == name.lower():
            return product
    return None


def add_product(inventory, name, price, quantity):
    """
    Add a new product to the inventory.
    Prevents duplicates.
    """
    # Check if product already exists
    if find_product(inventory, name):
        print(f"⚠️ '{name}' already exists.")
        return False

    # Add new product
    inventory.append({
        "name": name,
        "price": price,
        "quantity": quantity
    })

    print(f"✅ '{name}' added successfully.")
    return True


def show_inventory(inventory):
    """
    Display all products in a formatted way.
    """
    if not inventory:
        print("📭 Inventory is empty.")
        return

    print("\n📦 CURRENT INVENTORY")
    print("-" * 45)

    for product in inventory:
        print(
            f"Name: {product['name']:<20} "
            f"Price: ${product['price']:<10.2f} "
            f"Quantity: {product['quantity']}"
        )

    print("-" * 45)


def update_product(inventory, name, new_price=None, new_quantity=None):
    """
    Update price and/or quantity of an existing product.
    """
    product = find_product(inventory, name)

    if product:
        # Update values only if provided
        if new_price is not None:
            product["price"] = new_price

        if new_quantity is not None:
            product["quantity"] = new_quantity

        return True

    return False


def delete_product(inventory, name):
    """
    Remove a product from the inventory.
    """
    product = find_product(inventory, name)

    if product:
        inventory.remove(product)
        return True

    return False


def calculate_statistics(inventory):
    """
    Calculate general inventory statistics.

    Returns:
        dict | None
    """
    if not inventory:
        return None

    # Lambda function to calculate subtotal
    subtotal = lambda p: p["price"] * p["quantity"]

    # Total units and value
    total_units = sum(p["quantity"] for p in inventory)
    total_value = sum(subtotal(p) for p in inventory)

    # Find max values
    most_expensive = max(inventory, key=lambda p: p["price"])
    highest_stock = max(inventory, key=lambda p: p["quantity"])

    return {
        "total_units": total_units,
        "total_value": total_value,
        "most_expensive": (most_expensive["name"], most_expensive["price"]),
        "highest_stock": (highest_stock["name"], highest_stock["quantity"])
    }