from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/<code>')
def home(code=None):
    if code is None:
        return 'Hello world'
    return f'You tiped {code}'


if __name__ == '__main__':
    app.run()
