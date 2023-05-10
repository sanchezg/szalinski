from flask import Flask

from src.container import Container

from .application.controllers import main


def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    app.container = Container()
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
