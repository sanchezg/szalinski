# szalinski

Hey there! Welcome to Szalinski URL shortener!

First of all: why "Szalinski"? Well, that's the guy who shrunk their entire family in the late '80s movie :)

## Running instructions

You'll need docker and compose. Clone or download this project and build the images with:

```
docker-compose -f docker/docker-compose.yml build
```

Run the webapp with:

```
docker-compose -f docker/docker-compose.yml -p8000:8000 up
```

With a browser, go to `http://localhost:8000/` and enjoy the movie :)

## Development

Preferred way to run for debug and development is using docker compose. Otherwise I suggest you to create a virtualenv and install everything needed with poetry: `poetry install`

Build the environment using docker-compose and then run a shell with:

```
docker-compose -f docker/docker-compose.yml -p8000:8000 run /bin/bash
```

Inside the running container, run tests with:

```
poetry run pytest -sv tests/
```

Run development server with:

```
FLASK_DEBUG=1 poetry run flask --app src/app.py run --host=0.0.0.0 --port=8000
```
