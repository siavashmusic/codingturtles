from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


@views.route('/')
def index():
    return render_template("index.html", login=True)


@views.route("/html")
def html():
    courseData = [
        {"courseID": "html", "title": "HTML – An introduction", "desc": "Hypertext Markup Language) is the most basic building block of the Web. It defines the meaning and structure of web content. Other technologies besides HTML are generally used to describe a web page's appearance/presentation (CSS) or functionality/behaviour (JavaScript). 'Hypertext' refers to links that connect web pages to one another, either within a single website or between websites. Links are a fundamental aspect of the Web. By uploading content to the Internet and linking it to pages created by other people, you become an active participant in the World Wide Web. ",
         "img": "whatishtml.png", "postBy": "admin", "pubDate": " JUL 5TH '22", "link": "https://www.w3schools.com/html/html_intro.asp"},
        {"courseID": "html", "title": "HTML Elements",
         "desc": "A CSS rule consists of selector and declaration blocks.", "img": "elementtag.png",
         "postBy": "admin", "pubDate": " JUL 5TH '22", "link": "https://www.w3schools.com/html/html_elements.asp"},
        {"courseID": "html", "title": "HTML Attributes ",
         "desc": "A CSS selector selects the HTML element(s) you want to style. CSS selectors are used to 'find'(or select) the HTML elements you want to style. We can divide CSS selectors into five categories:",
         "img": "htmlattr.png", "postBy": "admin", "pubDate": " JUL 5TH '22", "link": "https://www.w3schools.com/html/html_attributes.asp"},
        {"courseID": "html", "title": "HTML Headings",
         "desc": "The CSS background properties are used to add background effects for elements, these include colour, image, how often they repeat and attachments, for example to set the background colour it would look like the following: ",
         "img": "headingtag.png", "postBy": "admin", "pubDate": " JUL 5TH '22", "link": "https://www.w3schools.com/html/html_headings.asp"},
        {"courseID": "html", "title": "HTML Paragraphs",
         "desc": "he border-style property specifies what kind of border to display.",
         "img": "ptag.png", "postBy": "admin", "pubDate": " JUL 5TH '22", "link": "https://www.w3schools.com/html/html_paragraphs.asp"},
        {"courseID": "html", "title": "HTML Lists",
         "desc": "he border-style property specifies what kind of border to display.",
         "img": "listtag.png", "postBy": "admin", "pubDate": " JUL 5TH '22", "link": "https://www.w3schools.com/html/html_lists.asp"},
    ]

    return render_template("articles.html", courseData=courseData)


@views.route("/css/")
def css(title="CSS_Syntax"):
    courseData = [
        {"courseID": "css", "title": "WHAT IS CSS?", "desc": "CSS stands for Cascading Style Sheets, it describes how HTML elements are to be displayed on screen, paper or in other media. CSS saves a lot of work, it can control the layout of multiple web pages all at once. CSS is used to define styles for your web pages, including design, layout and variations in display for different devices and screen sizes.",
         "img": "whatiscss.png", "postBy": "admin", "pubDate": " JUL 5TH '22" , "link": "https://www.w3schools.com/css/css_intro.asp"},
        {"courseID": "css", "title": "CSS SYNTAX",
         "desc": "A CSS rule consists of selector and declaration blocks.", "img": "syntax.png",
         "postBy": "admin", "pubDate": " JUL 5TH '22", "link": "https://www.w3schools.com/css/css_syntax.asp"},
        {"courseID": "css", "title": "CSS SELECTORS",
         "desc": "A CSS selector selects the HTML element(s) you want to style. CSS selectors are used to 'find'(or select) the HTML elements you want to style. We can divide CSS selectors into five categories:",
         "img": "select.png", "postBy": "admin", "pubDate": " JUL 5TH '22", "link": "https://www.w3schools.com/css/css_selectors.asp"},
        {"courseID": "css", "title": "CSS BACKGROUNDS",
         "desc": "The CSS background properties are used to add background effects for elements, these include colour, image, how often they repeat and attachments, for example to set the background colour it would look like the following: ",
         "img": "CSSBackgrounds.png", "postBy": "admin", "pubDate": " JUL 5TH '22", "link": "https://www.w3schools.com/css/css_background.asp"},
        {"courseID": "css", "title": "CSS BORDERS",
         "desc": "he border-style property specifies what kind of border to display.",
         "img": "cssborder.png", "postBy": "admin", "pubDate": " JUL 5TH '22", "link": "https://www.w3schools.com/css/css_border.asp"},
    ]

    return render_template("articles.html", courseData=courseData, title=title)


@views.route("/sql")
def sql():
    courseData = [
        {"courseID": "sql", "title": "WHAT IS SQL?", "desc": "Structured Query Language is a computer language that we use to interact with a relational database. SQL is a tool for organizing, managing, and retrieving archived data from a computer database. The original name was given by IBM as Structured English Query Language, abbreviated by the acronym SEQUEL. When data needs to be retrieved from a database, SQL is used to make the request. The DBMS processes the SQL query retrieves the requested data and returns it to us. Rather, SQL statements describe how a collection of data should be organized or what data should be extracted or added to the database.",
         "img": "whatissql.png", "postBy": "admin", "pubDate": " JUL 5TH '22", "link": "https://www.w3schools.com/sql/sql_intro.asp"},
        {"courseID": "sql", "title": "SQL SELECT ",
         "desc": "The SELECT statement is used to select data from a database. The data returned is stored in a result table, called the result-set. The SELECT DISTINCT statement is used to return only distinct (different) values. Inside a table, a column often contains many duplicate values; and sometimes you only want to list the different (distinct) values.",
         "img": "sqlselect.png","postBy": "admin", "pubDate": " JUL 5TH '22", "link": "https://www.w3schools.com/sql/sql_select.asp"},
        {"courseID": "sql", "title": "SQL WHERE ",
         "desc": "The WHERE clause is used to filter records. It is used to extract only those records that fulfil a specified condition, EG: ",
         "img": "sqlwhere.png", "postBy": "admin", "pubDate": " JUL 5TH '22", "link": "https://www.w3schools.com/sql/sql_where.asp"},
        {"courseID": "sql", "title": "The SQL AND, OR and NOT Operators",
         "desc": "The WHERE clause can be combined with AND, OR, and NOT operators. The AND and OR operators are used to filter records based on more than one condition:  ",
         "img": "sqlandor.png", "postBy": "admin", "pubDate": " JUL 5TH '22", "link": "https://www.w3schools.com/sql/sql_and_or.asp"},
        {"courseID": "sql", "title": "THE SQL Order by Keyword ",
         "desc": "The ORDER BY keyword is used to sort the result-set in ascending or descending order. The ORDER BY keyword sorts the records in ascending order by default. To sort the records in descending order, use the DESC keyword. ",
         "img": "orderbykey.png", "postBy": "admin", "pubDate": " JUL 5TH '22", "link": "https://www.w3schools.com/sql/sql_orderby.asp"},
        {"courseID": "sql", "title": "The SQL INSERT INTO statement",
         "desc": "A comment in PHP code is a line that is not executed as a part of the program. Its only purpose is to be read by someone who is looking at the code.",
         "img": "sqlinsert.png", "postBy": "admin", "pubDate": " JUL 5TH '22", "link": "https://www.w3schools.com/sql/sql_insert.asp"},
    ]
    return render_template("articles.html", courseData=courseData)


@views.route("/php")
def php():
    courseData = [
        {"courseID": "php", "title": "WHAT IS PHP?", "desc": "PHP is an acronym for 'PHP: Hypertext Pre-processor', it is a widely used open-source scripting language. These PHP scripts are executed on the servers. PHP is powerful enough to be at the core of the biggest blogging system on the web (word press) and is deep enough to run large social networks. PHP can generate dynamic page content and open, read, write, delete and close files on the server. PHP can collect form data, send and receive cookies and add, delete and modify data in your database. Data can be encrypted by PHP; it can be used to control user-access.  ",
         "img": "whatisphp.png", "postBy": "admin", "pubDate": " JUL 5TH '22", "link": "https://www.w3schools.com/php/php_intro.asp"},
        {"courseID": "php", "title": "PHP SYNTAX",
         "desc": "The structure which defines PHP computer language is called PHP syntax. The PHP script is executed on the server and the HTML result is sent to the browser. It can normally have HTML and PHP tags. PHP or Hypertext Pre-processor is a widely used open-source general-purpose scripting language and can be embedded with HTML. PHP files are saved with the '.php' extension. PHP scripts can be written anywhere in the document within PHP tags along with normal HTML.  ",
         "img": "phpsyntax.png","postBy": "admin", "pubDate": " JUL 5TH '22", "link": "https://www.w3schools.com/sql/sql_insert.asp"},
        {"courseID": "php", "title": "PHP VARIABLES ",
         "desc": "TVariables in a program are used to store some values or data that can be used later in a program. The variables are also like containers that store character values, numeric values, memory addresses, and strings. PHP has its own way of declaring and storing variables. There are a few rules, that need to be followed and facts that need to be kept in mind while dealing with variables in PHP.",
         "img": "phpvar.png", "postBy": "admin", "pubDate": " JUL 5TH '22", "link": "https://www.w3schools.com/php/php_syntax.asp"},
        {"courseID": "php", "title": "PHP OUTPUT",
         "desc": "With PHP, there are two basic ways to get output, both very similar to one another: echo and print. They are both used to output data to the screen. The differences are small: echo has no return value while print has a return value of 1 so it can be used in expressions. echo can take multiple parameters (although such usage is rare) while print can take one argument. echo is marginally faster than print. ",
         "img": "phpoutput.png", "postBy": "admin", "pubDate": " JUL 5TH '22", "link": "https://www.w3schools.com/php/php_echo_print.asp"},
        {"courseID": "php", "title": "PHP DATA TYPES",
         "desc": "Variables can store data of different types, and different data types can do different things. ",
         "img": "phpdatatypes.png", "postBy": "admin", "pubDate": " JUL 5TH '22", "link": "https://www.w3schools.com/php/php_datatypes.asp"},
        {"courseID": "php", "title": "PHP COMMENTS",
         "desc": "A comment in PHP code is a line that is not executed as a part of the program. Its only purpose is to be read by someone who is looking at the code.",
         "img": "phpcomment.png", "postBy": "admin", "pubDate": " JUL 5TH '22", "link": "https://www.w3schools.com/php/php_comments.asp"},
    ]
    return render_template("articles.html", courseData=courseData)


@views.route("/javascript")
def javascript():
    
    courseData = [
        {"courseID": "javascript", "title": "Introduction to JAVASCRIPT", "desc": "JavaScript is a cross-platform, object-oriented scripting language used to make webpages interactive (e.g., having complex animations, clickable buttons, popup menus, etc.). There are also more advanced server side versions of JavaScript such as Node.js, which allow you to add more functionality to a website than downloading files (such as realtime collaboration between multiple computers). Inside a host environment (for example, a web browser), JavaScript can be connected to the objects of its environment to provide programmatic control over them.",
         "img": "whatisjs.png", "postBy": "admin", "pubDate": " JUL 5TH '22", "link": "https://www.w3schools.com/js/js_intro.asp"},
        {"courseID": "javascript", "title": "JAVASCRIPT SYNTAX",
         "desc": "The basic goal of the Cascading Stylesheet (CSS) language is to allow a browser engine to paint elements of the page with specific features, like colors, positioning, or decorations. ",
         "img": "jssyntax.png","postBy": "admin", "pubDate": " JUL 5TH '22", "link": "https://www.w3schools.com/js/js_syntax.asp"},
        {"courseID": "javascript", "title": "JAVASCRIPT COMMENTS",
         "desc": "The Comment interface represents textual notations within markup; although it is generally not visually shown, such comments are available to be read in the source view.",
         "img": "jscomment.png", "postBy": "admin", "pubDate": " JUL 5TH '22", "link": "https://www.w3schools.com/js/js_comments.asp"},
        {"courseID": "javascript", "title": "JAVASCRIPT VARIABLES",
         "desc": "A variable is a container for a value, like a number we might use in a sum, or a string that we might use as part of a sentence.",
         "img": "jsval.png", "postBy": "admin", "pubDate": " JUL 5TH '22", "link": "https://www.w3schools.com/js/js_variables.asp"},
        {"courseID": "javascript", "title": "JavaScript Let",
         "desc": "let allows you to declare variables that are limited to the scope of a block statement, or expression on which it is used, unlike the var keyword, which declares a variable globally, or locally to an entire function regardless of block scope. The other difference between var and let is that the latter can only be accessed after its declaration is reached (see temporal dead zone). For this reason, let declarations are commonly regarded as non-hoisted.",
         "img": "jslet.png", "postBy": "admin", "pubDate": " JUL 5TH '22", "link": "https://www.w3schools.com/js/js_let.asp"},
        {"courseID": "javascript", "title": "JS const",
         "desc": "The const declaration creates block-scoped constants, much like variables declared using the let keyword. The value of a constant can't be changed through reassignment (i.e. by using the assignment operator), and it can't be redeclared (i.e. through a variable declaration). However, if a constant is an object or array its properties or items can be updated or removed.",
         "img": "jsconst.png", "postBy": "admin", "pubDate": " JUL 5TH '22", "link": "https://www.w3schools.com/js/js_const.asp"},
    ]
    return render_template("articles.html", courseData=courseData)

@views.route("/contactus")
# @login_required
def contactus():


    return render_template("contactus.html")

@views.route("/mentor/")
def mentor():
    mentors = [
        {"mentorID": "HTML&CSS", "mentor_name": "Cameron Williamson", "skills": "HTML&CSS", "img": "person-1.jpg",
         "about": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Facilis, perspiciatis repellat maxime, adipisci non ipsam at itaque rerum vitae, necessitatibus nulla animi expedita cumque provident inventore? Voluptatum in tempora earum deleniti, culpa odit veniam, ea reiciendis sunt ullam temporibus aut!"},
        {"mentorID": "HTML&CSS", "mentor_name": "Wade Warren", "skills": "Database", "img": "person-2.jpg",
         "about": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Facilis, perspiciatis repellat maxime, adipisci non ipsam at itaque rerum vitae, necessitatibus nulla animi expedita cumque provident inventore? Voluptatum in tempora earum deleniti, culpa odit veniam, ea reiciendis sunt ullam temporibus aut!"},
        {"mentorID": "HTML&CSS", "mentor_name": "Jane Cooper", "skills": "Python", "img": "person-3.jpg",
         "about": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Facilis, perspiciatis repellat maxime, adipisci non ipsam at itaque rerum vitae, necessitatibus nulla animi expedita cumque provident inventore? Voluptatum in tempora earum deleniti, culpa odit veniam, ea reiciendis sunt ullam temporibus aut!"},
        {"mentorID": "HTML&CSS", "mentor_name": "John Doe", "skills": "Javascript", "img": "person-4.jpg",
         "about": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Facilis, perspiciatis repellat maxime, adipisci non ipsam at itaque rerum vitae, necessitatibus nulla animi expedita cumque provident inventore? Voluptatum in tempora earum deleniti, culpa odit veniam, ea reiciendis sunt ullam temporibus aut!"},
        {"mentorID": "HTML&CSS", "mentor_name": "Allan W.", "skills": "Web Design", "img": "person-5.jpg",
         "about": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Facilis, perspiciatis repellat maxime, adipisci non ipsam at itaque rerum vitae, necessitatibus nulla animi expedita cumque provident inventore? Voluptatum in tempora earum deleniti, culpa odit veniam, ea reiciendis sunt ullam temporibus aut!"},
        {"mentorID": "HTML&CSS", "mentor_name": "Adam D.", "skills": "PHP&MYSQL", "img": "person-6.jpg",
         "about": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Facilis, perspiciatis repellat maxime, adipisci non ipsam at itaque rerum vitae, necessitatibus nulla animi expedita cumque provident inventore? Voluptatum in tempora earum deleniti, culpa odit veniam, ea reiciendis sunt ullam temporibus aut!"},
    ]
    return render_template("mentor.html", mentors=mentors)



@views.route("/quiz")
# @login_required
def quiz():
    courseData = [
        {"courseID": "sql", "title": "Test Your SQL Skills: 5-Question Quiz", "desc": "Challenge yourself and see how much you know about SQL with this 5-question quiz. Covering the basics of SQL syntax and operations, this quiz is perfect for both beginners and more advanced users looking to sharpen their skills. Test your knowledge and see where you stand in the world of SQL. Start now!",
         "img": "quiztime.png", "postBy": "admin", "pubDate": " Feb 2023", "link": "/quizsql"},
        {"courseID": "html", "title": "HTML Fundamentals: A 5-Question Challenge",
         "desc": "Put your HTML knowledge to the test with this 5-question quiz. Covering the basics of HTML syntax, elements, and attributes, this quiz is perfect for anyone looking to assess their understanding of this essential web development technology. Start now!",
         "img": "quiztime.png","postBy": "admin", "pubDate": " Feb 2023", "link": "/quizhtml"},
        {"courseID": "css", "title": "CSS Styling: A 5-Question Assessment",
         "desc": "Assess your CSS skills with this 5-question quiz. Covering topics such as selectors, properties, and layout, this quiz is a great way to see how much you know about this important aspect of web development. Start now!",
         "img": "quiztime.png", "postBy": "admin", "pubDate": " Feb 2023", "link": "quizcss"},
        {"courseID": "javascript", "title": "JavaScript Fundamentals: A 5-Question Evaluation",
         "desc": "Evaluate your JavaScript skills with this 5-question quiz. Covering topics such as variables, functions, and control structures, this quiz is a great way to see how much you know about this essential client-side scripting language. Start now!",
         "img": "quiztime.png", "postBy": "admin", "pubDate": "Feb 2023", "link": "quizjavascript"},
        {"courseID": "php", "title": "PHP Programming: A 5-Question Test",
         "desc": "Test your PHP programming knowledge with this 5-question quiz. Covering topics such as variables, loops, and functions, this quiz is a great way to assess your understanding of this powerful server-side scripting language. Start now!",
         "img": "quiztime.png", "postBy": "admin", "pubDate": " Feb 2023", "link": "quizphp"},
        ]

    return render_template("quiz.html", courseData=courseData)


@views.route("/quizsql")
# @login_required
def quizsql():


    return render_template("quizsql.html")


@views.route("/quizhtml")
# @login_required
def quizhhtml():

    return render_template("quizhtml.html")


@views.route("/quizcss")
# @login_required
def quizcss():


    return render_template("quizcss.html")


@views.route("/quizjavascript")
# @login_required
def quizjavascript():

    return render_template("quizjavascript.html")


@views.route("/quizphp")
# @login_required
def quizphp():

    return render_template("quizphp.html")


@views.route("/mastering_html")
# @login_required
def mastering_html():

    return render_template("mastering_html.html")


@views.route("/flexbox")
# @login_required
def flexbox():

    return render_template("flexbox.html")

@views.route("/anonymous_func")
# @login_required
def anonymous_func():

    return render_template("ann_func.html")

@views.route("/design_pattern")
# @login_required
def design_pattern():

    return render_template("design_pattern.html")

@views.route("/orm")
# @login_required
def orm():

    return render_template("orm.html")