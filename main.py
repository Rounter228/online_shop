import sqlite3

conn = sqlite3.connect('online_shop.db')
cursor = conn.cursor()

cursor.execute(''' 
CREATE TABLE IF NOT EXISTS products(
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL
)''')           

cursor.execute('''
CREATE TABLE IF NOT EXISTS customers(
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE 
)''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS orders(
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    order_date DATE NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
)''')


while True:
    print("0. Exit")
    print("1. Add product")
    num = int(input("Enter your choice: "))
    if num == 0:
        break
    elif num == 1:
        name = str(input("Enter product name: "))
        category = str(input("Enter product category: "))
        price = int(input("Enter product price: "))
        cursor.execute("INSERT INTO products (name, category, price) VALUES (?, ?, ?)", (name, category, price))
        conn.commit()