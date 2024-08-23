# import bibliothèque flask et création application flask
from flask import render_template, request, current_app, send_from_directory
app = current_app


@app.route("/robots.txt")
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route("/", methods=["GET", "POST"])
@app.route("/index/", methods=["GET", "POST"])
def index():
    return render_template("index.html")