# import bibliothèque flask et création application flask
from flask import render_template, request, current_app, send_from_directory
app = current_app
liste_categorie = ['Accueil','Réseaux','Web','Data','About']



@app.route("/robots.txt")
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route("/", methods=["GET", "POST"])
@app.route("/index/", methods=["GET", "POST"])
def Accueil():
    return render_template("index.html",liste_categorie=liste_categorie,categorie=liste_categorie[0])

@app.route("/reseaux/", methods=["GET", "POST"])
def Réseaux():
    return render_template("reseaux_intro.html",categorie=liste_categorie[1],liste_categorie=liste_categorie)

@app.route("/web/", methods=["GET", "POST"])
def Web():
    return render_template("web_intro.html",categorie=liste_categorie[2],liste_categorie=liste_categorie)
1
@app.route("/data/", methods=["GET", "POST"])
def Data():
    return render_template("data_intro.html",categorie=liste_categorie[3],liste_categorie=liste_categorie)

@app.route("/about/", methods=["GET", "POST"])
def About():
    return render_template("about.html",categorie=liste_categorie[4],liste_categorie=liste_categorie)