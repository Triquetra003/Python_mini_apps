# Inventory Management System

This is a simple command-line Inventory Management System that uses an Excel sheet (`Inventory.xlsx`) to store and manage inventory data. It allows users to view, add, update, and delete inventory items in a persistent and user-friendly way.

---

## Features

- **View Inventory**: Display all inventory items in a tabular format.
- **Add Item**: Add a new product by entering details like Product ID, Name, Category, Quantity, and Price.
- **Delete Item**: Delete a product by its Product ID after user confirmation.
- **Update Item**: Update the Category, Quantity, or Price of an existing product.
- **Exit**: Exit the program.

All changes are automatically saved to `Inventory.xlsx`.

---

## Data Format

The Excel file uses the following columns:

| Product ID | Product Name | Category   | Quantity | Price | Last Updated       |
|------------|--------------|------------|----------|-------|--------------------|
|            |              |            |          |       |                    |

---

## Requirements

- Python 3.7 or higher  
- Required Python packages:
  - `pandas`

Install using:

```bash
pip install pandas
```

---

## How to Run

- Make sure `Inventory.xlsx` is in the same folder as your python script.
- **Run the script:**
```bash
python inventory-management.py
```
- Follow the on-screen prompts to manage your inventory

---

## Planned Features

- Automatically create an excel sheet with pre-defined columns if one dosen't exist in the same directory
- Input validation for numbers or duplicate entries
- Low-stock warnings
- Search by name/category
- Export Summary reports

