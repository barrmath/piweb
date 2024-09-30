from flask import current_app
from werkzeug.middleware.proxy_fix import ProxyFix

app = current_app

# utilisation d'un proxy

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)