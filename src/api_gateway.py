from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('/workspaces/marketplace_listing/database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/products', methods=['GET'])
def get_products():
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products').fetchall()
    conn.close()
    return jsonify([dict(product) for product in products])

@app.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    conn = get_db_connection()
    product = conn.execute('SELECT * FROM products WHERE id = ?', (product_id,)).fetchone()
    conn.close()
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify(dict(product))

@app.route('/product', methods=['POST'])
def add_product():
    new_product = request.get_json()
    conn = get_db_connection()
    conn.execute('''
        INSERT INTO products (sku, title, description, price, metadata)
        VALUES (?, ?, ?, ?, ?)
    ''', (new_product['sku'], new_product['title'], new_product['description'], new_product['price'], new_product['metadata']))
    conn.commit()
    conn.close()
    return jsonify(new_product), 201

if __name__ == '__main__':
    app.run(debug=True)
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    files = request.files.getlist('files')
    for file in files:
        file.save(os.path.join('/workspaces/marketplace_listing/uploads', file.filename))
    return jsonify({'message': 'Files uploaded successfully'})
