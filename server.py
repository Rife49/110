from flask import Flask, jsonify, request
from http import HTTPStatus
import uuid


app = Flask(__name__) # Instance of Flask


# http://127.0.0.1:5000/home
@app.route("/home", methods=["GET"])
def home():
    return {"message": "Welcome to my world"}

# http://127.0.0.1:5000/greet-students
@app.route("/greet-students", methods=["GET"])
def say_hi():
    return{"message": "Hello Guys"}

@app.route("/cohort-66", methods=["GET"])
def get_students_66():
    student_list = ["Ariana", "Jesse", "Rife", "Leo"]
    return student_list

@app.route("/course", methods=["GET"])
def get_student_information():
    course_information = {
        "title": "Flask",
        "duration": "4 sessions",
        "level": "Beginner"
    }
    return course_information

@app.route("/user", methods=["GET"])
def get_user_info():
    user_info = {
        "name": "Rife",
        "role": "student",
        "is_active": "True",
        "favorite_technology": "TV"
    }
    return user_info

# ------ Products --------
products = [
    {
        "id": "1",
        "title": "Nintendo Switch",
        "price": "499.99",
        "category": "Electonics",
        "images": "https://picsum.photos/300/200?random=1"
    },
    {
        "id": "2",
        "title": "Smart Refrigerator",
        "price": "999.99",
        "category": "Electonics",
        "images": "https://picsum.photos/300/200?random=1"
    },
    {
        "id": "3",
        "title": "Bluetooth Speaker",
        "price": "79.99",
        "category": "Electonics",
        "images": "https://picsum.photos/300/200?random=1"
    }
    
]

# http://127.0.0.1:5000/api/products
@app.route("/api/products", methods=["GET"])
def get_products():
    return jsonify({"data": products}), HTTPStatus.OK


# --- Path Parameters ----
# -- /greet/<type:name>
@app.route("/greet/<string:name>", methods=["GET"])
def greet(name):
    return f"Hello {name}", HTTPStatus.OK

# http://127.0.0.1:5000/api/products/2
@app.route("/api/products/<string:product_id>", methods=["GET"])
def get_product_by_id(product_id):
    for product in products:
        if product ["id"] == product_id:
            return jsonify({
                "success": True,
                "message": "Product retrieved successfully",
                "data": product
            }), HTTPStatus.OK
    
    return jsonify({
        "success": False,
        "message": "Product not found",
    }), HTTPStatus.NOT_FOUND
    
    
# Post http://127.0.0.1:5000/api/products
@app.route("/api/products", methods=["POST"])
def create_products():
    print(f"request information {request.get_json()}")
    new_product = request.get_json()
    new_product["id"] = str(uuid.uuid4())
    products.append(new_product)
    return jsonify({
        "success": True,
        "message": "Product Successfully added",
        "data": new_product
    }), HTTPStatus.CREATED #201





# ---- Coupons -----
coupons = [
    {"_id": 1, "code": "WELCOME10", "discount": 10},
    {"_id": 2, "code": "SPOOKY25", "discount": 25},
    {"_id": 3, "code": "VIP50", "discount": 50}
]

@app.route("/api/coupons", methods=["GET"])
def get_coupons():
    return coupons, HTTPStatus.OK

@app.route("/api/coupons/count", methods=["GET"])
def get_coupons_count():
    coupons_counter = len(coupons)
    return jsonify({"coupons-counter": coupons_counter}), HTTPStatus.OK


# ------ Coupons Assignment 2 -------
coupons = [
    {"_id": "1", "code": "WELCOME10", "discount": 10},
    {"_id": "2", "code": "SPOOKY25", "discount": 25},
    {"_id": "3", "code": "VIP50", "discount": 50}
]


@app.route("/api/coupons", methods=["POST"])
def add_coupon():
    print(f"request information {request.get_json()}")
    add_coupon = request.get_json()
    add_coupon["id"] = str(uuid.uuid4())
    coupons.append(add_coupon)
    return jsonify({
        "message": "Coupon Successfully added",
        "data": add_coupon
    }), HTTPStatus.CREATED #201
    
    
app.route("/api/coupons", methods=["GET"])
def get_coupons():
    return coupons, HTTPStatus.OK


@app.route("/api/coupons/count/str:product_id>", methods=["GET"])
def coupons_count():
    coupons_counter = len(coupons)
    return jsonify({"coupons-counter": coupons_counter}), HTTPStatus.OK


# PUT http://127.0.0.1:5000/api/products



# DELETE http://127.0.0.1:5000/api/products






if __name__== "__main__": 
    app.run(debug=True)
    # when this file is run directly: __name__ == "__main__"
    # When this file is imported as module: __name__ == "server.py"
    
    