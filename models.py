from database import get_connection


# -------------------------
#   CUSTOMERS CRUD
# -------------------------

def add_customer(name, phone, email, password, address):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO customers (name, phone, email, password, address)
    VALUES (?, ?, ?, ?, ?)
    """, (name, phone, email, password, address))

    conn.commit()
    conn.close()


def update_customer(customer_id, name, phone, email, address):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    UPDATE customers
    SET name = ?, phone = ?, email = ?, address = ?
    WHERE id = ?
    """, (name, phone, email, address, customer_id))

    conn.commit()
    conn.close()


def delete_customer(customer_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM customers WHERE id = ?", (customer_id,))

    conn.commit()
    conn.close()


def get_all_customers():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM customers")
    rows = cur.fetchall()

    conn.close()
    return rows


def get_customer_by_id(customer_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM customers WHERE id = ?", (customer_id,))
    row = cur.fetchone()

    conn.close()
    return row


# -------------------------
#   PRODUCTS CRUD
# -------------------------

def add_product(name, price, stock, image_path):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO products (name, price, stock, image_path)
    VALUES (?, ?, ?, ?)
    """, (name, price, stock, image_path))

    conn.commit()
    conn.close()


def update_product(product_id, name, price, stock, image_path):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    UPDATE products
    SET name = ?, price = ?, stock = ?, image_path = ?
    WHERE id = ?
    """, (name, price, stock, image_path, product_id))

    conn.commit()
    conn.close()


def delete_product(product_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM products WHERE id = ?", (product_id,))

    conn.commit()
    conn.close()


def get_all_products():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM products")
    rows = cur.fetchall()

    conn.close()
    return rows


def get_product_by_id(product_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM products WHERE id = ?", (product_id,))
    row = cur.fetchone()

    conn.close()
    return row


# -------------------------
#   ORDERS (basic)
# -------------------------

def add_order(customer_id, total_amount, order_number, date):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO orders (customer_id, total_amount, order_number, date)
    VALUES (?, ?, ?, ?)
    """, (customer_id, total_amount, order_number, date))

    conn.commit()
    conn.close()
