from unicodedata import name
from flask import Flask, render_template, request, session
app = Flask(__name__)
app.secret_key = "Velicraptors were actually chickens"

@app.route ("/")
def index():
    return render_template("index.html")


@app.route("/result", methods=["post"])
def result():
    print ("Got Post Info")
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comment"] = request.form["comment"]
    print ("name", "location", "language", "comment")
    return render_template ("result.html", name_on_template = session["name"], location_on_template =session["location"], language_on_template = session["language"], comment_on_template = session["comment"])


if __name__ == '__main__':
    app.run(debug=True)