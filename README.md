


# 📦 Inventory Management System (Python)

## 📌 Overview

This project is a modular **Inventory Management System** built in Python. It allows users to manage products, perform CRUD operations, calculate statistics, and persist data using CSV files.

The system is designed following good practices such as:

* Modular architecture
* Separation of concerns
* Input validation
* Error handling

---

## 🚀 Features

* Add, update, delete, and search products
* Display full inventory
* Calculate business statistics
* Save inventory to CSV files
* Load inventory from CSV with validation
* Merge or overwrite data when loading

---

## 🧱 Project Structure

```
app.py           # Main menu and program execution
services.py      # Business logic (CRUD + statistics)
file_manager.py  # CSV read/write operations
```

---

## 📊 Data Structure

Each product is stored as a dictionary inside a list:

```python
{
    "name": str,
    "price": float,
    "quantity": int
}
```

---

## 📈 Statistics Calculated

* Total units
* Total inventory value
* Most expensive product
* Product with highest stock

---

## 💾 CSV Format

The system uses CSV files with the following structure:

```
name,price,quantity
```

---

## ▶️ How to Run

1. Open terminal
2. Navigate to project folder
3. Run:

```
python app.py
```

---

## 🛡️ Error Handling

* Invalid numeric inputs
* File not found
* Encoding errors
* Invalid CSV format
* Negative values

---

## 📌 Author Notes

This project was developed as part of a programming assignment focused on:

* Python collections (lists, dictionaries, tuples)
* Modular programming
* File persistence

---

## 📌 Note

The English-translated code is provided separately from this README to follow best practices.

---
## Install

git clone https://github.com/JromeroRodriguez/Historia-de-usuario-M1S3.git

---

## ✅ Final Status

✔ Fully functional project
✔ Meets requirements
✔ Clean and modular code
✔ Ready for submission
