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
    """This is the get_trades function
    Its a simple method that finds trades from
    the database and then lists in an accordian
    on the trades.html page
    """
    trades = list(mongo.db.trades.find())
    return render_template("trades.html", trades=trades)


@app.route("/search", methods=["GET", "POST"])
def search():
    """This is the Search function
    The Search method has two methods,
    1. The GET method gets the infromation from the input query
    2. The POST method then uses the infromation from the query
    and searches from the search index in database
    """
    query = request.form.get("query")
    trades = list(mongo.db.trades.find({"$text": {"$search": query}}))
    return render_template("trades.html", trades=trades)


@app.route("/register", methods=["GET", "POST"])
def register():
    """This is the Register function
    The Register method has two methods,
    1. The GET method gets the infromation from the input when
    a user inputs username and password
    2. The POST method then uses the infromation from the user
    and then implements into the database, as long as their
    information passes requirments
    """
    if request.method == "POST":
        """ check if username is already exists in DB """
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    """This is the Login function
    The Login method has two methods,
    1. The GET method gets the infromation from the input when
    a user inputs username and password
    2. The POST method checks with the database to see if
    the username exists
    """

    if request.method == 'POST':

        # check if username exists in db

        existing_user = \
            mongo.db.users.find_one(
                {'username': request.form.get('username').lower()})

        if existing_user:

            # ensure hashed password matches user input

            if check_password_hash(existing_user['password'],
                                   request.form.get('password')):
                session['user'] = request.form.get('username').lower()
                flash('Welcome, {}'.format(request.form.get('username')))
                return redirect(url_for('profile',
                                username=session['user']))
            else:

                # invalid password match

                flash('Incorrect Username and/or Password')
                return redirect(url_for('login'))
        else:

            # username doesn't exist

            flash('Incorrect Username and/or Password')
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """This is the profile function
    The profile method has two methods, and also checks for
    the username session
    1. The GET method gets the infromation from the input when
    a user inputs username and password, also grabs the session
    Id
    2. The POST method then takes the session ID from username
    and then prints all the trades in assoication with with the
    usernmae
    """
    trades = list(mongo.db.trades.find({"created_by": session["user"]}))
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template(
            "profile.html", username=username, trades=trades)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """Logout method removes the user from the
    session and then redirects them back to the
    Login template"""
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_trade", methods=["GET", "POST"])
def add_trade():
    """The add trade funbction has two methods
    1. The Get method uses the login infromation for the user
    2. The Post method takes all information for adding a trade in
    a dictionary and then correctly matches them up with the DB variables
    """
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
    """ This is where the user is able to make any chnages to the trade
    It uses a Get and Post method as well, in addition to using the
    trade-id.
    The Get method passes along the Trade_id thats unique to the trade
    Then with the Post method just like the add_trade it adds it
    to the dictionary and re-enters it into the database
    """
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


@app.route("/delete_trade/<trade_id>")
def delete_trade(trade_id):
    """ The delete trade funtuion
    is a simple function which uses the unique variable from
    the add_trade. When a trade is marked as sold, users
    use this function so it gets removed from the trades.html template
    """
    mongo.db.trades.remove({"_id": ObjectId(trade_id)})
    flash("Trade Succesfully Sold")
    return redirect(url_for("get_trades"))


@app.route("/get_consoles")
def get_consoles():
    """Get_consoles finds all the dirrent console names"""
    console_type = list(mongo.db.console_type.find().sort("console_name", 1))
    return render_template("consoles.html", console_type=console_type)


@app.route("/add_console", methods=["GET", "POST"])
def add_console():
    """If the Admin wants to add anoher console to the platfrom
    All it does is fetches thier credentials and then allows them access
    to the console.html. Here they can add console names into the database
    """
    if request.method == "POST":
        console = {
            "console_name": request.form.get("console_name")
        }
        mongo.db.console_type.insert_one(console)
        flash("New Console was Added")
        return redirect(url_for("get_consoles"))

    return render_template("add_console.html")


@app.route("/delete_console/<console_id>")
def delete_console(console_id):
    """ At the delete_console function
    The admins can easily delete console names for whatever reason.
    It uses the uniuqe variable console_id to make sure it gets
    implemented in the database
    """
    mongo.db.console_type.remove({"_id": ObjectId(console_id)})
    flash("Trade Category Succesfully Deleted!")
    return redirect(url_for("get_consoles"))


# Invald url
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
