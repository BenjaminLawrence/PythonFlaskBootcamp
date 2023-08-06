# Import flask
from flask import Flask, render_template
# Intialize flask object, __name__ is resolved to __main__
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Welcome</h1> <p>Under construction</p>"

@app.route("/about")
def about():
    return "About Us"

@app.route("/profile/<name>")
def profile_page(name):
    return "<h2>Welcome to profile " + name + "</h2>"

@app.route("/first-template")
def first_template():
    return render_template("first_template.html")

if __name__ == '__main__':
    app.run()
