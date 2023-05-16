# szalinski

Hey there! Welcome to Szalinski URL shortener!

First of all: why "Szalinski"? Well, that's the guy who shrunk their entire family in the late '80s [movie](https://en.wikipedia.org/wiki/Honey,_I_Shrunk_the_Kids) :)

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
poetry uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

## Design and considerations

The app was developed with FastAPI, MongoDB and Redis using a DDD approach.

**Why FastAPI?**

The initial approach was to use Flask because it is lightweight, but since Flask async support is poor and it is not _really_ async, I went with FastAPI.

**Why MongoDB?**

Since the initial data is not structured and there is no need to have it in the near future, MongoDB offers a good scalability for this particular case.

**Why Redis?**

MongoDB is not enough if we want to provide a _really_ fast response. Here comes Redis as a cache storage: it provides a quick access to data.

### Code design (DDD, DI & Repo pattern)

The codebase was entirely developed using DDD, where I can easily identify these layers (from upper layers to the lower ones):

1. Application (`src/application`): Where the code that is closer to the user lives. That is: routes (or views).
2. Domain (`src/domain`): Where the business logic lives. Here we have the loosely coupled services: each service performs only one specific thing. Also they don't depend on infra concerns and don't know nothing about how lower levels are implemented. Note that code here depends on repositories abstractions instead implementations.
3. Infrastructure (`src/infra`): The actual implementation of repositories using corresponding libraries to access the different infrastructure services (MongoDB or Redis).

DI was also used with dependency-injector package to keep coupling low and instead inject objects already initialized.

Take a look into `pyproject.toml` file to know the involved libraries for each case.
