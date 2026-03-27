# File Manager Module
# Handles CSV file operations (save and load inventory data)

import csv


def save_csv(inventory, path, include_header=True):
    """
    Save inventory data into a CSV file.

    Args:
        inventory (list): List of product dictionaries
        path (str): Destination file path
        include_header (bool): Include header row in CSV
    """

    # Prevent saving if inventory is empty
    if not inventory:
        print(" Inventory is empty. Nothing to save.")
        return

    try:
        # Open file in write mode
        with open(path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            # Write header if enabled
            if include_header:
                writer.writerow(["name", "price", "quantity"])

            # Write each product as a row
            for product in inventory:
                writer.writerow([
                    product["name"],
                    product["price"],
                    product["quantity"]
                ])

        print(f" Inventory saved at: {path}")

    except PermissionError:
        print(f" Permission denied: {path}")

    except Exception as e:
        print(f" Error saving file: {e}")


def load_csv(path):
    """
    Load inventory data from a CSV file with validations.

    Args:
        path (str): File path

    Returns:
        list: List of valid product dictionaries
    """

    inventory = []
    invalid_rows = 0  # Counter for invalid rows

    try:
        # Open file in read mode
        with open(path, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)

            # Validate header format
            header = next(reader)
            if header != ["name", "price", "quantity"]:
                print(" Invalid header format. Expected: name,price,quantity")
                return []

            # Process each row
            for row in reader:
                try:
                    # Ensure correct number of columns
                    if len(row) != 3:
                        raise ValueError

                    name = row[0].strip()
                    price = float(row[1])
                    quantity = int(row[2])

                    # Validate non-negative values
                    if price < 0 or quantity < 0:
                        raise ValueError

                    # Add valid product to inventory
                    inventory.append({
                        "name": name,
                        "price": price,
                        "quantity": quantity
                    })

                except (ValueError, IndexError):
                    # Count invalid rows
                    invalid_rows += 1

        # Show warning if invalid rows were skipped
        if invalid_rows > 0:
            print(f" {invalid_rows} invalid row(s) skipped.")

        return inventory

    except FileNotFoundError:
        print(f" File not found: {path}")

    except UnicodeDecodeError:
        print(" Encoding error. Use UTF-8 format.")

    except Exception as e:
        print(f" Unexpected error: {e}")

    return []