from application import Flask, app\
    # , mysql
from flask import render_template, request, url_for, redirect, flash
from werkzeug.security import check_password_hash, generate_password_hash

@app.route("/")
def index():
    return render_template("index.html", login= True)


@app.route("/html")
def html():
    return render_template("articles.html")


@app.route("/css/")
@app.route("/css/<title>")                                                                                                                                                                                                                                                                                                                                                                               
def css(title="CSS_Syntax"):
    courseData = [
            {"courseID":"css", "title":"CSS Syntax", "desc": "A CSS rule consists of a selector and a declaration block.", "img":"cssSyntax.png", "postBy": "admin", "pubDate":" JUL 5TH '22" },
            {"courseID":"css", "title":"CSS Selectors", "desc": "A CSS selector selects the HTML element(s) you want to style.", "img":"CSSSelectors.png", "postBy": "admin", "pubDate":" JUL 5TH '22" },
            {"courseID":"css", "title":"CSS Backgrounds", "desc": "The CSS background properties are used to add background effects for elements.", "img":"CSSBackgrounds.png", "postBy": "admin", "pubDate":" JUL 5TH '22" },
            {"courseID":"css", "title":"CSS Borders", "desc": "The CSS border properties allow you to specify the style, width, and color of an element's border.", "img":"CSSBorders.png", "postBy": "admin", "pubDate":" JUL 5TH '22" },
    ]
    
    return render_template("articles.html", courseData=courseData, title=title)


@app.route("/sql")
def sql():
    return render_template("articles.html")


@app.route("/php")
def php():
    return render_template("articles.html")


@app.route("/javascript")
def javascript():
    return render_template("articles.html")


@app.route("/signup/", methods=['POST', 'GET'])
# @app.route("/register")
# @app.route("/registration")
def signup():


    return render_template('signup.html')


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/mentor/")
def mentor():
    
    mentors = [
            {"mentorID":"HTML&CSS", "mentor_name":"Cameron Williamson", "skills": "HTML&CSS", "img":"person-1.jpg", "about": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Facilis, perspiciatis repellat maxime, adipisci non ipsam at itaque rerum vitae, necessitatibus nulla animi expedita cumque provident inventore? Voluptatum in tempora earum deleniti, culpa odit veniam, ea reiciendis sunt ullam temporibus aut!" },
            {"mentorID":"HTML&CSS", "mentor_name":"Wade Warren", "skills": "Database", "img":"person-2.jpg", "about": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Facilis, perspiciatis repellat maxime, adipisci non ipsam at itaque rerum vitae, necessitatibus nulla animi expedita cumque provident inventore? Voluptatum in tempora earum deleniti, culpa odit veniam, ea reiciendis sunt ullam temporibus aut!" },
            {"mentorID":"HTML&CSS", "mentor_name":"Jane Cooper", "skills": "Python", "img":"person-3.jpg", "about": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Facilis, perspiciatis repellat maxime, adipisci non ipsam at itaque rerum vitae, necessitatibus nulla animi expedita cumque provident inventore? Voluptatum in tempora earum deleniti, culpa odit veniam, ea reiciendis sunt ullam temporibus aut!" },
            {"mentorID":"HTML&CSS", "mentor_name":"John Doe", "skills": "Javascript", "img":"person-4.jpg", "about": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Facilis, perspiciatis repellat maxime, adipisci non ipsam at itaque rerum vitae, necessitatibus nulla animi expedita cumque provident inventore? Voluptatum in tempora earum deleniti, culpa odit veniam, ea reiciendis sunt ullam temporibus aut!" },
            {"mentorID":"HTML&CSS", "mentor_name":"Allan W.", "skills": "Web Design", "img":"person-5.jpg", "about": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Facilis, perspiciatis repellat maxime, adipisci non ipsam at itaque rerum vitae, necessitatibus nulla animi expedita cumque provident inventore? Voluptatum in tempora earum deleniti, culpa odit veniam, ea reiciendis sunt ullam temporibus aut!" },
            {"mentorID":"HTML&CSS", "mentor_name":"Adam D.", "skills": "PHP&MYSQL", "img":"person-6.jpg", "about": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Facilis, perspiciatis repellat maxime, adipisci non ipsam at itaque rerum vitae, necessitatibus nulla animi expedita cumque provident inventore? Voluptatum in tempora earum deleniti, culpa odit veniam, ea reiciendis sunt ullam temporibus aut!" },
    ]
    return render_template("mentor.html", mentors=mentors)

    