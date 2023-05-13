from flask import Flask

from src.application.controllers import main
from src.container import Container


def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    app.container = Container()
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
