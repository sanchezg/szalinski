from flask import Flask

from src.container import Container

from .application.controllers import main

app = Flask(__name__)
app.register_blueprint(main)
app.container = Container()

if __name__ == '__main__':
    app.run()
