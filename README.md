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
