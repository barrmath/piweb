from flask import Flask


def create_app():
    app = Flask(__name__, static_folder="static")


    with app.app_context():
        app.config.from_object("config")
        import web_app.views

    return app