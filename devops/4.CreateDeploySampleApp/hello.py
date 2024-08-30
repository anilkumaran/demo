from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"




@app.route("/ecom")
def hello_ecom():
    return "<p>Hello, ecom!</p>"