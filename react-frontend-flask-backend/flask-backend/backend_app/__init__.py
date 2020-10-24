import os
from flask import Flask, request, make_response


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True) #instance path is where path of __init__.py is, with sub directory of 'instance'
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )
    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/hello")
    def hello():
        return "hello world"
    from . import db
    db.init_app(app)
    from . import api
    app.register_blueprint(api.bp)
    return app