import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# main page path 
@app.route("/")
@app.route("/get_cars")
def get_cars():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    cars = list(mongo.db.cars.find())
    return render_template("cars.html", cars=cars, categories=categories)

# search path
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    cars = list(mongo.db.cars.find({"$text": {"$search": query}}))
    if cars:
        flash("Your Car is Found")
    else:
        flash("No Results Found")

    return render_template("cars.html", cars=cars, categories=categories)

# register path
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("get_cars", username=session["user"]))

    return render_template("register.html")

# login path
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")

# profile path
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    cars = list(mongo.db.cars.find())

    if session["user"]:
        return render_template("profile.html", username=username, cars=cars)

    return redirect(url_for("login"))

# logout path
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))

# add car path
@app.route("/add_car", methods=["GET", "POST"])
def add_car():
    if request.method == "POST":
        car = {
            "category_name": request.form.get("category_name"),
            "car_name": request.form.get("car_name").capitalize(),
            "car_model": request.form.get("car_model").capitalize(),
            "car_year": request.form.get("car_year"),
            "car_fuel": request.form.get("car_fuel").capitalize(),
            "car_image_url": request.form.get("car_image_url"),
            "created_by": session["user"].capitalize()
        }
        mongo.db.cars.insert_one(car)
        flash("Your Car Is Successfully Added")
        return redirect(url_for("get_cars"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template(
        "add_car.html", username=username, categories=categories)

# edit car path
@app.route("/edit_car/<car_id>", methods=["GET", "POST"])
def edit_car(car_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "car_name": request.form.get("car_name").capitalize(),
            "car_model": request.form.get("car_model").capitalize(),
            "car_year": request.form.get("car_year"),
            "car_fuel": request.form.get("car_fuel").capitalize(),
            "car_image_url": request.form.get("car_image_url"),
            "created_by": session["user"].capitalize()
        }
        mongo.db.cars.update({"_id": ObjectId(car_id)}, submit)
        flash("Car Successfully Updated")
        return redirect(url_for("get_cars"))

    car = mongo.db.cars.find_one({"_id": ObjectId(car_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_car.html", car=car, categories=categories)

# delete car path
@app.route("/delete_car/<car_id>")
def delete_car(car_id):
    mongo.db.cars.remove({"_id": ObjectId(car_id)})
    flash("Car Successfully Deleted")
    return redirect(url_for("get_cars"))

# categories path
@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template(
        "categories.html", categories=categories, username=username)

# add category path
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get(
                "category_name").capitalize(),
            "category_image_url": request.form.get(
                "category_image_url"),
            "category_description": request.form.get(
                "category_description").capitalize()
        }
        mongo.db.categories.insert_one(category)
        flash("Your Category Is Successfully Added")
        return redirect(url_for("get_categories"))
    
    return render_template("add_category.html")

# edit category path
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get(
                "category_name").capitalize(),
            "category_image_url": request.form.get(
                "category_image_url"),
            "category_description": request.form.get(
                "category_description").capitalize()
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Your Category Is Successfully Update")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)

# delete category path
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Your Category Is Successfully Deleted")
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
