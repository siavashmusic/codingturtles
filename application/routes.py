from application import app
from flask import render_template

@app.route("/")
def index():
    return render_template("index.html", login= True)


@app.route("/html")
def html():
    return render_template("articles.html")


@app.route("/css")
def css():
    courseData = [
        {"courseID":"css", "title":"CSS Syntax", "desc": "A CSS rule consists of a selector and a declaration block.", "img":"static/img/cssSyntax.png", "postBy": "admin", "pubDate":" JUL 5TH '22" },
        {"courseID":"css", "title":"CSS Selectors", "desc": "A CSS selector selects the HTML element(s) you want to style.", "img":"static/img/CSSSelectors.png", "postBy": "admin", "pubDate":" JUL 5TH '22" },
        {"courseID":"css", "title":"CSS Backgrounds", "desc": "The CSS background properties are used to add background effects for elements.", "img":"static/img/CSSBackgrounds.png", "postBy": "admin", "pubDate":" JUL 5TH '22" },
        {"courseID":"css", "title":"CSS Borders", "desc": "The CSS border properties allow you to specify the style, width, and color of an element's border.", "img":"static/img/CSSBorders.png", "postBy": "admin", "pubDate":" JUL 5TH '22" },
    
    ]
    print(courseData)
    return render_template("articles.html", courseData=courseData)


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
# @app.route("/register")
# @app.route("/registration")
def signup():
    return render_template("signup.html", login=True)


@app.route("/login")
def login():
    return render_template("login.html")