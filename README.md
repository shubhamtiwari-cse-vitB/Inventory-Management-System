# Inventory Management System

## 📌 Project Overview

The **Inventory Management System** is a Python and MySQL based application designed to manage product information, purchases, and invoices.

The system provides a menu-driven interface through which users can perform different inventory-related operations such as adding, searching, updating, deleting and sorting products, recording purchases, and managing invoice records.

---

## 🎯 Objectives

- To maintain product information in a database.
- To make product searching and management easier.
- To record purchase details systematically.
- To maintain invoice information.
- To provide a simple menu-driven inventory management system.
- To use Python with MySQL for database-based application development.

---

## ✨ Features

### 📦 Product Management
- Add new products
- Display product details
- Search for products
- Delete products
- Update product information
- Sort products by different fields

### 🛒 Purchase Management
- Record product purchases
- Store customer information
- Store quantity and pricing details
- Maintain purchase records

### 🧾 Invoice Management
- Generate invoice records after purchases
- Store invoice information
- Display invoice records
- Manage stored invoice records

### 📊 Records
- View product information
- View purchase history
- View invoice records

---

## 🛠️ Technologies Used

- **Python**
- **MySQL**
- **MySQL Connector/Python**

---

## 🗄️ Database

The project uses a MySQL database named:

`himalaya`

The system works with the following tables:

- `product`
- `purchase`
- `invoice`

### Product Table

Stores information such as:

- Product name
- Product number
- Stock
- Quantity to be produced
- MRP
- Rate
- Manufacturing date
- Expiry date

### Purchase Table

Stores:

- Product name
- Number of units
- MRP
- Rate
- Customer name

### Invoice Table

Stores:

- Product name
- Number of units
- MRP
- Rate
- Customer name
- Amount

---

## ⚙️ Requirements

Before running the project, make sure you have:

- Python installed
- MySQL Server installed and running
- MySQL Connector for Python installed

Install the MySQL connector using:

```bash
pip install mysql-connector-python
