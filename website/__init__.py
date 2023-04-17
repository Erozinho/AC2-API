from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config ['SECRET KEY'] = '123123123'

    from website.formu import formu


    app.register_blueprint(formu, url_prefix="/")


    return app
