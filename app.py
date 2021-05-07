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


@app.route("/")
@app.route("/get_trades")
def get_trades():
    trades = list(mongo.db.trades.find())
    return render_template("trades.html", trades=trades)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username is already exists in DB
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
        flash("Sign Up was succesful")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


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


# The profile page is empty but create a way for users to see thier listings
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # rab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_trade", methods=["GET", "POST"])
def add_trade():
    if request.method == "POST":
        is_negotiable = "on" if request.form.get("is_negotiable") else "off"
        trade = {
            "console_name": request.form.get("console_name"),
            "game_name": request.form.get("game_name"),
            "trade_desc": request.form.get("trade_desc"),
            "is_negotiable": is_negotiable,
            "gamer_tag": request.form.get("gamer_tag"),
            "created_by": session["user"]
        }
        mongo.db.trades.insert_one(trade)
        flash("Trade Successfully Listed")
        return redirect(url_for("get_trades"))

    console_type = mongo.db.console_type.find().sort("console_name", 1)
    return render_template("add_trade.html", console_type=console_type)


@app.route("/edit_trade/<trade_id>", methods=["GET", "POST"])
def edit_trade(trade_id):
    if request.method == "POST":
        is_negotiable = "on" if request.form.get("is_negotiable") else "off"
        submit = {
            "console_name": request.form.get("console_name"),
            "game_name": request.form.get("game_name"),
            "trade_desc": request.form.get("trade_desc"),
            "is_negotiable": is_negotiable,
            "gamer_tag": request.form.get("gamer_tag"),
            "created_by": session["user"]
        }
        mongo.db.trades.update({"_id": ObjectId(trade_id)}, submit)
        flash("Trade Successfully Updated")

    trade = mongo.db.trades.find_one({"_id": ObjectId(trade_id)})
    console_type = mongo.db.console_type.find().sort("console_name", 1)
    return render_template(
        "edit_trade.html", trade=trade, console_type=console_type)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
