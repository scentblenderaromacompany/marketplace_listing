import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def generate_sales_report(db_path):
    conn = sqlite3.connect(db_path)
    query = "SELECT title, price FROM products"
    df = pd.read_sql_query(query, conn)
    conn.close()

    plt.figure(figsize=(10, 6))
    plt.bar(df['title'], df['price'])
    plt.xlabel('Product')
    plt.ylabel('Price')
    plt.title('Sales Performance')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('/workspaces/marketplace_listing/reports/sales_performance.png')
    plt.show()

if __name__ == "__main__":
    db_path = "/workspaces/marketplace_listing/database.db"
    generate_sales_report(db_path)
