import sqlite3

def get_connection():
    return sqlite3.connect("store.db")

def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    # جدول مشتری‌ها
    cur.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT,
        email TEXT,
        password TEXT,
        address TEXT
    )
    """)

    # جدول محصولات
    cur.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        stock INTEGER NOT NULL,
        image_path TEXT
    )
    """)

    # جدول سفارش‌ها
    cur.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        total_amount REAL,
        order_number TEXT,
        date TEXT,
        FOREIGN KEY (customer_id) REFERENCES customers(id)
    )
    """)

    conn.commit()
    conn.close()
