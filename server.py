from flask import Flask

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

if __name__== "__main__": 
    app.run(debug=True)
    # when this file is run directly: __name__ == "__main__"
    # When this file is imported as module: __name__ == "server.py"
    
    