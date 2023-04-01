from flask import Flask, request, jsonify
import sqlite3
import os

db_folder = os.path.join(os.path.dirname(__file__), "products_db.db")

app = Flask(__name__)

def find_by_product_id(id):
    conn = sqlite3.connect(db_folder)
    sql = """
        SELECT *
        FROM products
        WHERE id=?
    """
    val = (id,)
    cursor = conn.execute(sql, val)
    columns = cursor.fetchone()
    record = {
        'id': columns[0],
        'name': columns[1],
        'category': columns[2],
        'price': columns[3],
        'instock': columns[4],
    }
    conn.close()
    return record

# Get all Products
@app.route('/products', methods=["GET"])
def get_products():
    data = []
    conn = sqlite3.connect(db_folder)
    sql = """
        SELECT *
        FROM products
        ORDER BY id
    """
    cursor = conn.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        record = {
            'id': row[0],
            'name': row[1],
            'category': row[2],
            'price': row[3],
            'instock': row[4]
        }
        data.append(record)
    conn.close()
    return data

# Get Product by Id
@app.route('/product/<id>', methods=["GET"])
def get_product_by_id(id):
    data =  find_by_product_id(id)
    return data

# Add Product
@app.route('/product', methods = ["POST"])
def post_product():
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    conn = sqlite3.connect(db_folder)
    sql = """
        INSERT INTO products(name, category, price, instock)
        VALUES(?, ?, ?, ?)
    """
    val = (name, category, price, instock, )
    conn.execute(sql, val)
    conn.commit()
    conn.close()
    return "Created successfully"

# Delete Product
@app.route('/product/<id>', methods = ['DELETE'])
def delete_product(id):
    data = find_by_product_id(id)
    if not data:
        return {"error": "product not found"}, 404
    else:
        conn = sqlite3.connect(db_folder)
        sql = """
            DELETE FROM products
            WHERE id=?
        """
        val = (id)
        conn.execute(sql, val)
        conn.commit()
        conn.close()
        return 'Deleted successfully'

@app.route('/product/<id>', methods = ["PUT"])
def patch_product(id):
    product = find_by_product_id(id)
    if not product:
        return {"error": "product not found"}, 404
    
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    conn = sqlite3.connect(db_folder)
    sql = """
        UPDATE products
        SET name=?, category=?, price=?, instock=?
        WHERE id=?
    """
    val = (name, category, price, instock, id)
    conn.execute(sql, val)
    conn.commit()
    conn.close()
    return "Updated successfully"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug= True) 