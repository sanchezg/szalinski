from gevent.pywsgi import WSGIServer

from src.app import create_app

app = create_app()
http_server = WSGIServer(("0.0.0.0", 8000), app)
http_server.serve_forever()
