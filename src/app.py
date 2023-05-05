from flask import Flask

from .application.controllers import main

app = Flask(__name__)
app.register_blueprint(main)

if __name__ == '__main__':
    app.run()
