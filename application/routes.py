from application import app
from flask import render_template

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/css")
def css():
    return render_template("css.html")


@app.route("/html")
def html():
    return render_template("html.html")


@app.route("/sql")
def sql():
    return render_template("sql.html")


@app.route("/php")
def php():
    return render_template("php.html")


@app.route("/javascript")
def javascript():
    return render_template("javascript.html")


@app.route("/signup")
@app.route("/register")
@app.route("/registration")
def signup():
    return render_template("signup.html", login=False)


@app.route("/login")
def login():
    return render_template("login.html")