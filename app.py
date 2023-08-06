# Import flask
from flask import Flask
# Intialize flask object, __name__ is resolved to __main__
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Welcome</h1> <p>Under construction</p>"

@app.route("/about")
def about():
    return "About Us"

if __name__ == '__main__':
    app.run()
