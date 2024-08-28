# import bibliothèque flask et création application flask
from flask import render_template, request, current_app, send_from_directory

app = current_app

liste_categorie = ['Accueil','Réseaux','Web','Data','About']
liste_cotes_reseaux =['Autohébergement','Monitoring','Kube','Proxy','Certificat']
liste_cotes_web =[]
liste_cotes_data =[]


@app.route("/robots.txt")
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route("/", methods=["GET", "POST"])
@app.route("/index/", methods=["GET", "POST"])
def Accueil():
    return render_template("index.html",liste_categorie=liste_categorie,categorie=liste_categorie[0])

####################################################### Partie RESEAUX  ###############################################################

@app.route("/reseaux/", methods=["GET", "POST"])
def Réseaux():
    return render_template("reseaux_intro.html"
                            ,categorie=liste_categorie[1]
                            ,liste_categorie=liste_categorie
                            ,liste_cotes_categorie=liste_cotes_reseaux)


@app.route("/reseaux/Auto-hebergement/", methods=["GET", "POST"])
def Autohébergement():
    return render_template("encours.html"
                            ,categorie=liste_categorie[1]
                            ,liste_categorie=liste_categorie
                            ,liste_cotes_categorie=liste_cotes_reseaux
                            ,categorie_cotes=liste_cotes_reseaux[0])


@app.route("/reseaux/Monitoring/", methods=["GET", "POST"])
def Monitoring():
    return render_template("encours.html"
                            ,categorie=liste_categorie[1]
                            ,liste_categorie=liste_categorie
                            ,liste_cotes_categorie=liste_cotes_reseaux
                            ,categorie_cotes=liste_cotes_reseaux[1])

@app.route("/reseaux/PodmanKube/", methods=["GET", "POST"])
def Kube():
    return render_template("encours.html"
                            ,categorie=liste_categorie[1]
                            ,liste_categorie=liste_categorie
                            ,liste_cotes_categorie=liste_cotes_reseaux
                            ,categorie_cotes=liste_cotes_reseaux[2])

@app.route("/reseaux/Proxy/", methods=["GET", "POST"])
def Proxy():
    return render_template("encours.html"
                            ,categorie=liste_categorie[1]
                            ,liste_categorie=liste_categorie
                            ,liste_cotes_categorie=liste_cotes_reseaux
                            ,categorie_cotes=liste_cotes_reseaux[3])

@app.route("/reseaux/Certificat/", methods=["GET", "POST"])
def Certificat():
    return render_template("encours.html"
                            ,categorie=liste_categorie[1]
                            ,liste_categorie=liste_categorie
                            ,liste_cotes_categorie=liste_cotes_reseaux
                            ,categorie_cotes=liste_cotes_reseaux[4])


####################################################### Partie WEB  ###################################################################

@app.route("/web/", methods=["GET", "POST"])
def Web():
    return render_template("web_intro.html"
                            ,categorie=liste_categorie[2]
                            ,liste_categorie=liste_categorie
                            ,liste_cotes_categorie=liste_cotes_web)



####################################################### Partie DATA  ##################################################################

@app.route("/data/", methods=["GET", "POST"])
def Data():
    return render_template("data_intro.html"
                            ,categorie=liste_categorie[3]
                            ,liste_categorie=liste_categorie
                            ,liste_cotes_categorie=liste_cotes_data)

####################################################### Partie ABOUT  ################################################################

@app.route("/about/", methods=["GET", "POST"])
def About():
    return render_template("about.html",categorie=liste_categorie[4],liste_categorie=liste_categorie)