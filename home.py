from flask import Flask, request, json, jsonify
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
db_path = os.path.join(os.path.dirname(__file__), "app.db")
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


some_dict = {"key1": "value 1", "is_active": False}


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    is_active = db.Column(db.Boolean, default=False)

    def get_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "is_active": self.is_active,
        }


@app.route("/")
def index():
    return "This is the index!"


@app.route("/hello/<username>")
def hello_world(username):
    return f"Hello {username}"


@app.route("/return", methods=["GET"])
def return_something():
    if request.method == "GET":
        return request.args.get("value")
    else:
        return "This is only a GET request!"


@app.route("/json")
def normal_json():
    return json.dumps(some_dict)


@app.route("/jsonify")
def jsonify_function():
    return jsonify(some_dict)


@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == "GET":
        users = User.query.all()
        result = [user.get_dict() for user in users]

    elif request.method == "POST":
        username = request.json["username"]
        email = request.json["email"]
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        result = user.get_dict()

    return jsonify(result)


@app.route("/user/<id>", methods=["GET", "PUT", "DELETE"])
def user(id):
    if request.method == "GET":
        user = User.query.get(id)
        result = user.get_dict()
        return jsonify(result)

    elif request.method == "PUT":
        user = User.query.get(id)
        if "username" in request.json:
            user.username = request.json["username"]
        if "email" in request.json:
            user.email = request.json["email"]
        if "is_active" in request.json:
            user.is_active = request.json["is_active"]
        db.session.add(user)
        db.session.commit()
        return jsonify(user.get_dict())

    elif request.method == "DELETE":
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({"success": True})
