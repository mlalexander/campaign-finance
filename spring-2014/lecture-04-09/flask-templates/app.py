from flask import Flask
from flask import render_template, make_response
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/hello-template")
def hello_template():
    return render_template("hello.txt")

@app.route("/data")
def make_json():
    response = make_response(render_template("data.json"))
    response.headers['Content-Type'] = 'application/json'
    return response

if __name__ == "__main__":
    app.run()