from flask import Flask, request, jsonify

app = Flask(__name__)

products = [
    {"id":'1', "name":'Laptop', "category":'Electronics', "price": 30000, "instock": 200},
    {"id":'2', "name":'Smart Watch', "category":'Wearables', "price": 8000, "instock": 100},
    {"id":'3', "name":'Monitor', "category":'Electronics', "price": 12000, "instock": 150},
]

def find_by_product_id(id):
    data = [x for x in products if x ['id']==id]
    return data

def find_product_index(id):
    return next((i for i, x in enumerate(products) if x["id"] == id), None)

# Get all Products
@app.route('/products', methods=["GET"])
def get_products():
    return jsonify(products)

# Get Product by Id
@app.route('/product/<id>', methods=["GET"])
def get_product_by_id(id):
    data =  find_by_product_id(id)
    return jsonify(data)

# Add Product
@app.route('/product', methods = ["POST"])
def post_product():
    id = request.form.get('id')
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    new_data = {
        "id": id,
        "name": name,
        "category": category,
        "price": price,
        "instock": instock,
    }

    if (find_by_product_id(id)):
        return {"eror": "Product Already Exists."}, id
    else:
        products.append(new_data)
        return jsonify(products)

# Delete Product
@app.route('/product/<id>', methods = ['DELETE'])
def delete_product(id):
    data = find_by_product_id(id)
    if not data:
        return {"error": "product not found"}, 404
    else:
        products.remove(data[0]) 
        return products, 200

@app.route('/product/<id>', methods = ["PATCH"])
def patch_product(id):
    matching_index = find_product_index(id)
    if matching_index < 0:
        return {"error": "product not found"}, 404
    
    instock = request.form.get('instock')

    temp_product = products[matching_index]
    temp_product["instock"] = int(instock)
    products[matching_index] = temp_product

    return jsonify(products)

@app.route('/product/<id>', methods = ["PUT"])
def put_product(id):
    matching_index = find_product_index(id)
    if matching_index < 0:
        return {"error": "product not found"}, 404

    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    temp_product = products[matching_index]
    temp_product["name"] = name
    temp_product["category"] = category
    temp_product["price"] = int(price)
    temp_product["instock"] = int(instock)
    products[matching_index] = temp_product

    return jsonify(products)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug= True) 