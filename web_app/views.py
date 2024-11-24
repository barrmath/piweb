# import bibliothèque flask et création application flask
from flask import render_template, request, current_app, send_from_directory

app = current_app


@app.route("/robots.txt")
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


@app.route("/", methods=["GET", "POST"])
@app.route("/index/", methods=["GET", "POST"])
def Accueil():
    return render_template("index.html", menu=app.menu, page="about",next=app.menu[2][1],last=app.menu[0][0])


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", menu=app.menu, page="erreur404",next="",last=""), 404


####################################################### Partie RESEAUX  ###############################################################


@app.route("/reseaux/", methods=["GET", "POST"])
def Réseaux():
    return render_template("reseaux_intro.html", menu=app.menu, page="reseaux",next="",last="")


@app.route("/reseaux/Auto-hebergement/", methods=["GET", "POST"])
def Autohébergement():
    return render_template(
        "reseaux/autohebergement.html", menu=app.menu, page="reseaux",next=app.menu[1][2],last=app.menu[1][5])


@app.route("/reseaux/Monitoring/", methods=["GET", "POST"])
def Monitoring():
    return render_template("reseaux/monitoring.html", menu=app.menu, page="reseaux",next="",last="")


@app.route("/reseaux/Jenkins/", methods=["GET", "POST"])
def Jenkins():
    return render_template("/reseaux/Jenkins.html", menu=app.menu, page="reseaux",next="",last="")


@app.route("/reseaux/Proxy/", methods=["GET", "POST"])
def Proxy():
    return render_template("reseaux/proxy.html", menu=app.menu, page="reseaux",next=app.menu[1][5],last=app.menu[2][6])


@app.route("/reseaux/Certificat/", methods=["GET", "POST"])
def Certificat():
    return render_template("reseaux/certificats.html", menu=app.menu, page="reseaux",next=app.menu[1][1],last=app.menu[2][6])


####################################################### Partie WEB  ###################################################################


@app.route("/web/", methods=["GET", "POST"])
def Web():
    return render_template("web_intro.html", menu=app.menu, page="web",next="",last="")


@app.route("/web/git/", methods=["GET", "POST"])
def Git():
    return render_template("web/git.html", menu=app.menu, page="web",next=app.menu[2][2],last=app.menu[0][0])


@app.route("/web/HTMLCSS/", methods=["GET", "POST"])
def HTML():
    return render_template("web/htmlcss.html", menu=app.menu, page="web",next=app.menu[3][1],last=app.menu[2][1])


@app.route("/web/flask/", methods=["GET", "POST"])
def Flask():
    return render_template("web/Flask.html", menu=app.menu, page="web",next=app.menu[2][4],last=app.menu[3][2])


@app.route("/web/jinja/", methods=["GET", "POST"])
def Jinja():
    return render_template("web/jinja.html", menu=app.menu, page="web",next=app.menu[2][5],last=app.menu[2][3])


@app.route("/web/gunicorn/", methods=["GET", "POST"])
def Gunicorn():
    return render_template("web/gunicorn.html", menu=app.menu, page="web",next=app.menu[2][6],last=app.menu[2][4])


@app.route("/web/podman/", methods=["GET", "POST"])
def Podman():
    return render_template("web/podman.html", menu=app.menu, page="web",next=app.menu[1][4],last=app.menu[2][5])


####################################################### Partie DATA  ##################################################################


@app.route("/data/", methods=["GET", "POST"])
def Data():
    return render_template("data_intro.html", menu=app.menu, page="data",next="",last="")


@app.route("/data/SQL/", methods=["GET", "POST"])
def SQL():
    return render_template("data/sql.html", menu=app.menu, page="data",next=app.menu[3][2],last=app.menu[2][2])


@app.route("/data/python/", methods=["GET", "POST"])
def Python():
    return render_template("data/python.html", menu=app.menu, page="data",next=app.menu[2][3],last=app.menu[3][1])


@app.route("/data/pandas/", methods=["GET", "POST"])
def Pandas():
    return render_template("data/pandas.html", menu=app.menu, page="data",next="",last="")


@app.route("/data/graphique/", methods=["GET", "POST"])
def Graphique():
    return render_template("data/graphique.html", menu=app.menu, page="data",next="",last="")


####################################################### Partie ABOUT  ################################################################


@app.route("/about/", methods=["GET", "POST"])
def About():
    return render_template("about.html", menu=app.menu, page="about",next="",last="")
