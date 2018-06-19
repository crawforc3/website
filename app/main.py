from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello world"

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)