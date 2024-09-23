# import bibliothèque flask et création application flask
from flask import render_template, request, current_app, send_from_directory
from werkzeug.middleware.proxy_fix import ProxyFix

app = current_app

# utilisation d'un proxy a deplacer plus tard
app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

liste_categorie = ('Accueil','Réseaux','Web','Data','About')
liste_cotes_reseaux =('Autohébergement','Monitoring','Kube','Proxy','Certificat')
liste_cotes_web =('HTML','Flask','Jinja','Gunicorn','Podman')
liste_cotes_data =('SQL','Python','Pandas','Graphique')


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
    return render_template("reseaux/autohebergement.html"
                            ,categorie=liste_categorie[1]
                            ,liste_categorie=liste_categorie
                            ,liste_cotes_categorie=liste_cotes_reseaux
                            ,categorie_cotes=liste_cotes_reseaux[0])


@app.route("/reseaux/Monitoring/", methods=["GET", "POST"])
def Monitoring():
    return render_template("reseaux/monitoring.html"
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
    return render_template("reseaux/certificats.html"
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
                            ,liste_cotes_categorie=liste_cotes_web
                            )


@app.route("/web/HTMLCSS", methods=["GET", "POST"])
def HTML():
    return render_template("web/htmlcss.html"
                            ,categorie=liste_categorie[2]
                            ,liste_categorie=liste_categorie
                            ,liste_cotes_categorie=liste_cotes_web
                            ,categorie_cotes=liste_cotes_web[0])


@app.route("/web/flask", methods=["GET", "POST"])
def Flask():
    return render_template("web/Flask.html"
                            ,categorie=liste_categorie[2]
                            ,liste_categorie=liste_categorie
                            ,liste_cotes_categorie=liste_cotes_web
                            ,categorie_cotes=liste_cotes_web[1])

@app.route("/web/jinja", methods=["GET", "POST"])
def Jinja():
    return render_template("encours.html"
                            ,categorie=liste_categorie[2]
                            ,liste_categorie=liste_categorie
                            ,liste_cotes_categorie=liste_cotes_web
                            ,categorie_cotes=liste_cotes_web[2])

@app.route("/web/gunicorn", methods=["GET", "POST"])
def Gunicorn():
    return render_template("encours.html"
                            ,categorie=liste_categorie[2]
                            ,liste_categorie=liste_categorie
                            ,liste_cotes_categorie=liste_cotes_web
                            ,categorie_cotes=liste_cotes_web[3])

@app.route("/web/podman", methods=["GET", "POST"])
def Podman():
    return render_template("encours.html"
                            ,categorie=liste_categorie[2]
                            ,liste_categorie=liste_categorie
                            ,liste_cotes_categorie=liste_cotes_web
                            ,categorie_cotes=liste_cotes_web[4])

####################################################### Partie DATA  ##################################################################

@app.route("/data/", methods=["GET", "POST"])
def Data():
    return render_template("data_intro.html"
                            ,categorie=liste_categorie[3]
                            ,liste_categorie=liste_categorie
                            ,liste_cotes_categorie=liste_cotes_data)

@app.route("/data/SQL", methods=["GET", "POST"])
def SQL():
    return render_template("data/sql.html"
                            ,categorie=liste_categorie[3]
                            ,liste_categorie=liste_categorie
                            ,liste_cotes_categorie=liste_cotes_data
                            ,categorie_cotes=liste_cotes_data[0])

@app.route("/data/python", methods=["GET", "POST"])
def Python():
    return render_template("data/python.html"
                            ,categorie=liste_categorie[3]
                            ,liste_categorie=liste_categorie
                            ,liste_cotes_categorie=liste_cotes_data
                            ,categorie_cotes=liste_cotes_data[1])

@app.route("/data/pandas", methods=["GET", "POST"])
def Pandas():
    return render_template("encours.html"
                            ,categorie=liste_categorie[3]
                            ,liste_categorie=liste_categorie
                            ,liste_cotes_categorie=liste_cotes_data
                            ,categorie_cotes=liste_cotes_data[2])

@app.route("/data/graphique", methods=["GET", "POST"])
def Graphique():
    return render_template("encours.html"
                            ,categorie=liste_categorie[3]
                            ,liste_categorie=liste_categorie
                            ,liste_cotes_categorie=liste_cotes_data
                            ,categorie_cotes=liste_cotes_data[3])

####################################################### Partie ABOUT  ################################################################

@app.route("/about/", methods=["GET", "POST"])
def About():
    return render_template("about.html",categorie=liste_categorie[4],liste_categorie=liste_categorie)