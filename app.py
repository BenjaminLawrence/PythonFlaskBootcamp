# Import flask
from flask import Flask
# Intialize flask object, __name__ is resolved to __main__
app = Flask(__name__)

if __name__ == '__main__':
    app.run()

@app.route("/")
def home():
    return "Hello, Flask!"
