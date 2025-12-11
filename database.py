import sqlite3
from datetime import datetime

def get_connection():
    return sqlite3.connect("store.db")

def create_tables():
    conn = get_connection()
    cur = conn.cursor()

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

    cur.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        stock INTEGER NOT NULL,
        image_path TEXT
    )
    """)

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

# ---- seed helpers ----
def _insert_default_customers(cur):
    customers = [
        ("Sara Ahmadi", "09121234567", "sara@example.com", "1234", "Tehran"),
        ("Fatemeh Karimi", "09351234567", "fatemeh@example.com", "abcd", "Shiraz"),
        ("Abolfazl Rahimi", "09132223344", "hadi@example.com", "pass", "Isfahan"),
    ]
    cur.executemany("""
    INSERT INTO customers (name, phone, email, password, address)
    VALUES (?, ?, ?, ?, ?)
    """, customers)

def _insert_default_products(cur):
    products = [
        ("دستبند سنگی مشکی", 120000, 10, "images/bracelet_black.jpg"),
        ("گردنبند قلب نقره‌ای", 180000, 7, "images/necklace_silver.jpg"),
        ("ساعت مچی اسپرت زنانه", 350000, 5, "images/watch_sport.jpg"),
        ("گوشواره استیل طلایی", 90000, 12, "images/earring_gold.jpg"),
        ("کیف دوشی کوچک چرمی", 250000, 6, "images/bag_small.jpg"),
        ("ست انگشتر سه‌تایی دخترانه", 75000, 20, "images/ring_set.jpg"),
        ("تل دخترانه گل‌دار", 45000, 15, "images/hairband_flower.jpg"),
        ("اسکرانچی مخملی", 30000, 30, "images/scrunchie_velvet.jpg"),
    ]
    cur.executemany("""
    INSERT INTO products (name, price, stock, image_path)
    VALUES (?, ?, ?, ?)
    """, products)

def seed_initial_data_if_empty():
    """
    این تابع ایمن است و فقط زمانی داده‌ها را وارد می‌کند که جدول
    customers یا products خالی باشند.
    """
    conn = get_connection()
    cur = conn.cursor()

    # بررسی تعداد ردیف‌ها در هر جدول
    cur.execute("SELECT COUNT(*) FROM customers")
    customers_count = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM products")
    products_count = cur.fetchone()[0]

    did_insert = False

    if customers_count == 0:
        _insert_default_customers(cur)
        did_insert = True

    if products_count == 0:
        _insert_default_products(cur)
        did_insert = True

    if did_insert:
        conn.commit()

    conn.close()
    return did_insert  # برمی‌گرداند که آیا چیزی اضافه شده یا نه
