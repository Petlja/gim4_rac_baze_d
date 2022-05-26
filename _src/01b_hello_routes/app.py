from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
@app.route("/home")
def home():
    return "Home"
    
@app.route("/about")
def about():
    return "About"
