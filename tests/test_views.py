# teste si l'application envoie bien les pages avec la requete get et post


def test_racine_get_status_codeOK(client):
    response = client.get("/")
    assert response.status_code == 200


def test_racine_post_status_codeOK(client):
    response = client.post("/")
    assert response.status_code == 200


def test_index_get_status_codeOK(client):
    response = client.get("/index/")
    assert response.status_code == 200


def test_index_post_status_codeOK(client):
    response = client.post("/index/")
    assert response.status_code == 200


################################################## Party reseaux   ####################################################################


def test_intro_reseau_get_status_codeOK(client):
    response = client.get("/reseaux/")
    assert response.status_code == 200


def test_intro_reseaux_post_status_codeOK(client):
    response = client.post("/reseaux/")
    assert response.status_code == 200


def test_autohebergement_get_status_codeOK(client):
    response = client.get("/reseaux/Auto-hebergement/")
    assert response.status_code == 200


def test_autohebergement_post_status_codeOK(client):
    response = client.post("/reseaux/Auto-hebergement/")
    assert response.status_code == 200


def test_monitoring_get_status_codeOK(client):
    response = client.get("/reseaux/Monitoring/")
    assert response.status_code == 200


def test_monitoring_post_status_codeOK(client):
    response = client.post("/reseaux/Monitoring/")
    assert response.status_code == 200


def test_podmanKube_get_status_codeOK(client):
    response = client.get("/reseaux/PodmanKube/")
    assert response.status_code == 200


def test_podmanKube_post_status_codeOK(client):
    response = client.post("/reseaux/PodmanKube/")
    assert response.status_code == 200


def test_Proxy_get_status_codeOK(client):
    response = client.get("/reseaux/Proxy/")
    assert response.status_code == 200


def test_Proxy_post_status_codeOK(client):
    response = client.post("/reseaux/Proxy/")
    assert response.status_code == 200


def test_Certificat_get_status_codeOK(client):
    response = client.get("/reseaux/Certificat/")
    assert response.status_code == 200


def test_Certificat_post_status_codeOK(client):
    response = client.post("/reseaux/Certificat/")
    assert response.status_code == 200


####################################################### Partie WEB  ###################################################################


def test_web_intro_get_status_codeOK(client):
    response = client.get("/web/")
    assert response.status_code == 200


def test_web_git_get_status_codeOK(client):
    response = client.get("/web/git/")
    assert response.status_code == 200


def test_web_intro_post_status_codeOK(client):
    response = client.post("/web/")
    assert response.status_code == 200


def test_html_css_get_status_codeOK(client):
    response = client.get("/web/HTMLCSS/")
    assert response.status_code == 200


def test_html_css_post_status_codeOK(client):
    response = client.post("/web/HTMLCSS/")
    assert response.status_code == 200


def test_flask_get_status_codeOK(client):
    response = client.get("/web/flask/")
    assert response.status_code == 200


def test_flask_post_status_codeOK(client):
    response = client.post("/web/flask/")
    assert response.status_code == 200


def test_jinja_get_status_codeOK(client):
    response = client.get("/web/jinja/")
    assert response.status_code == 200


def test_jinja_post_status_codeOK(client):
    response = client.post("/web/jinja/")
    assert response.status_code == 200


def test_gunicorn_get_status_codeOK(client):
    response = client.get("/web/gunicorn/")
    assert response.status_code == 200


def test_gunicorn_post_status_codeOK(client):
    response = client.post("/web/gunicorn/")
    assert response.status_code == 200


def test_podman_get_status_codeOK(client):
    response = client.get("/web/podman/")
    assert response.status_code == 200


def test_podman_post_status_codeOK(client):
    response = client.post("/web/podman/")
    assert response.status_code == 200


####################################################### Partie DATA  ##################################################################


def test_data_intro_get_status_codeOK(client):
    response = client.get("/data/")
    assert response.status_code == 200


def test_data_intro_post_status_codeOK(client):
    response = client.post("/data/")
    assert response.status_code == 200


def test_sql_get_status_codeOK(client):
    response = client.get("/data/SQL/")
    assert response.status_code == 200


def test_sql_post_status_codeOK(client):
    response = client.post("/data/SQL/")
    assert response.status_code == 200


def test_python_get_status_codeOK(client):
    response = client.get("/data/python/")
    assert response.status_code == 200


def test_python_post_status_codeOK(client):
    response = client.post("/data/python/")
    assert response.status_code == 200


def test_pandas_get_status_codeOK(client):
    response = client.get("/data/pandas/")
    assert response.status_code == 200


def test_pandas_post_status_codeOK(client):
    response = client.post("/data/pandas/")
    assert response.status_code == 200


def test_graphique_get_status_codeOK(client):
    response = client.get("/data/graphique/")
    assert response.status_code == 200


def test_graphique_post_status_codeOK(client):
    response = client.post("/data/graphique/")
    assert response.status_code == 200


####################################################### Partie ABOUT  ################################################################


def test_about_get_status_codeOK(client):
    response = client.get("/about/")
    assert response.status_code == 200


def test_about_post_status_codeOK(client):
    response = client.post("/about/")
    assert response.status_code == 200
