from flask import Flask, request, jsonify

app = Flask(__name__)

countries = [
    {"id":'1', "name":'Thailand', "capital":'Bangkok'},
    {"id":'2', "name":'Sri Lanka', "capital":'Colombo'},
    {"id":'3', "name":'USA', "capital":'LA'},
]

def find_next_id(id):
    data = [x for x in countries if x ['id']==id]
    return data

@app.route('/country', methods=["GET"])
def get_country():
    return jsonify(countries)

@app.route('/country/<id>', methods=["GET"])
def get_country_id(id):
    data =  find_next_id(id)
    return jsonify(data)

@app.route('/country', methods = ["POST"])
def post_country():
    id = request.form.get('id')
    name = request.form.get('name')
    capital = request.form.get('capital')

    new_data = {
        "id": id,
        "name": name,
        "capital": capital
    }

    if (find_next_id(id)):
        return {"eror": "Bad Request"}, id
    else:
        countries.append(new_data)
        return jsonify(countries)

#DELETE
@app.route('/country/<id>', methods = ['DELETE'])
def delete_country(id):

    data = find_next_id(id)
    if not data:
        return {"error": "Country not found"}, 404
    else:
        countries.remove(data[0]) 
        return "Country deleted succuessfully" ,200

@app.route('/country/<id>', methods = ["PATCH"])
def patch_country(id):
    capital = request.form.get('capital')
    matching_index = next((i for i, x in enumerate(countries) if x["id"] == id), None)
    current_country = countries[matching_index]
    current_country["capital"] = capital
    countries[matching_index] = current_country
    return jsonify(countries)

@app.route('/country/<id>', methods = ["PUT"])
def put_country(id):
    name = request.form.get('name')
    capital = request.form.get('capital')
    matching_index = next((i for i, x in enumerate(countries) if x["id"] == id), None)
    current_country = countries[matching_index]
    current_country["name"] = name
    current_country["capital"] = capital
    countries[matching_index] = current_country
    return jsonify(countries)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port =5000, debug= True) 