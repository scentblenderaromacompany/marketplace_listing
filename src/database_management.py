import sqlite3

def create_database(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sku TEXT NOT NULL UNIQUE,
            title TEXT,
            description TEXT,
            price REAL,
            metadata TEXT
        )
    ''')
    conn.commit()
    conn.close()
    print(f"Database created at {db_path}")

def add_product_to_database(db_path, sku, title, description, price, metadata):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''
        INSERT INTO products (sku, title, description, price, metadata)
        VALUES (?, ?, ?, ?, ?)
    ''', (sku, title, description, price, metadata))
    conn.commit()
    conn.close()
    print(f"Product {sku} added to database")

if __name__ == "__main__":
    db_path = "/workspaces/marketplace_listing/database.db"
    create_database(db_path)
    add_product_to_database(db_path, "SKU_00001", "Sample Title", "Sample Description", 19.99, '{"key": "value"}')
