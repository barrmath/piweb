# import bibliothèque flask et création application flask
from flask import render_template, request, current_app, send_from_directory

app = current_app

menu = (('Accueil','Accueil')
        ,("Réseaux",'Autohébergement','Monitoring','Kube','Proxy','Certificat')
        ,('Web','HTML','Flask','Jinja','Gunicorn','Podman')
        ,('Data','SQL','Python','Pandas','Graphique')
        ,('About','About'))

@app.route("/robots.txt")
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route("/", methods=["GET", "POST"])
@app.route("/index/", methods=["GET", "POST"])
def Accueil():
    return render_template("index.html",menu=menu)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html",menu=menu), 404

####################################################### Partie RESEAUX  ###############################################################

@app.route("/reseaux/", methods=["GET", "POST"])
def Réseaux():
    return render_template("reseaux_intro.html",menu=menu)


@app.route("/reseaux/Auto-hebergement/", methods=["GET", "POST"])
def Autohébergement():
    return render_template("reseaux/autohebergement.html",menu=menu)


@app.route("/reseaux/Monitoring/", methods=["GET", "POST"])
def Monitoring():
    return render_template("reseaux/monitoring.html",menu=menu)

@app.route("/reseaux/PodmanKube/", methods=["GET", "POST"])
def Kube():
    return render_template("encours.html",menu=menu)

@app.route("/reseaux/Proxy/", methods=["GET", "POST"])
def Proxy():
    return render_template("encours.html",menu=menu)

@app.route("/reseaux/Certificat/", methods=["GET", "POST"])
def Certificat():
    return render_template("reseaux/certificats.html",menu=menu)


####################################################### Partie WEB  ###################################################################

@app.route("/web/", methods=["GET", "POST"])
def Web():
    return render_template("web_intro.html",menu=menu)

@app.route("/web/HTMLCSS/", methods=["GET", "POST"])
def HTML():
    return render_template("web/htmlcss.html",menu=menu)

@app.route("/web/flask/", methods=["GET", "POST"])
def Flask():
    return render_template("web/Flask.html",menu=menu)

@app.route("/web/jinja/", methods=["GET", "POST"])
def Jinja():
    return render_template("web/jinja.html",menu=menu)

@app.route("/web/gunicorn/", methods=["GET", "POST"])
def Gunicorn():
    return render_template("encours.html",menu=menu)

@app.route("/web/podman/", methods=["GET", "POST"])
def Podman():
    return render_template("encours.html",menu=menu)

####################################################### Partie DATA  ##################################################################

@app.route("/data/", methods=["GET", "POST"])
def Data():
    return render_template("data_intro.html",menu=menu)

@app.route("/data/SQL/", methods=["GET", "POST"])
def SQL():
    return render_template("data/sql.html",menu=menu)

@app.route("/data/python/", methods=["GET", "POST"])
def Python():
    return render_template("data/python.html",menu=menu)

@app.route("/data/pandas/", methods=["GET", "POST"])
def Pandas():
    return render_template("data/pandas.html",menu=menu)

@app.route("/data/graphique/", methods=["GET", "POST"])
def Graphique():
    return render_template("data/graphique.html",menu=menu)

####################################################### Partie ABOUT  ################################################################

@app.route("/about/", methods=["GET", "POST"])
def About():
    return render_template("about.html",menu=menu)