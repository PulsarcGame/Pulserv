# Pulserv ~ A serverside platform for Pulsarc.

## Aims:
- Map Database
- Nice pretty project website
- Player Ranking Platform, similar to Intralism's khb-soft.ru

## Stack:

- Flask + Mongoengine

## To Run:

```
python3 run_web.py
# or
python3 run_api.py
```

## More Details:

The server will communicate with the client over a semi-RESTful API design, the client will request a token from the server using login details, password and username cannot be used aside from initial token request.

The server itself will store Map files in raw binary, packaged into .psm archives (a renamed zip)

There will be three major platforms supported by the server
  - Online, browsable catalog (Highest Priority)
  - Ingame, API powered catalog (Still high priority)
  - PulseMan, A package manager, used for development, testing, and potentially baked into the PulseArc game.

## Stuff to know about:

The web server will allow uploads of .psm files via the /map/upload endpoint, this will be matched by the api server.
Upon a .psm upload, the file is unzipped, if it fails the endpoint returns an error of "invalid mapfile"
The unzipping occurs via the __init__ method of the MapPackage class
Each unzipped file's raw bytes are passed into their own respective instances of beatMap, beatAudio, and backgoundImage
Which then perform their own processing via their own __init__ methods.
They then store their respective meta as instance properties.

The upload endpoint then builds a mapStore object with metadata from the generated MapPackage object
and stores the raw in a FileField on that object.

The mapStore object is then saved to mongoDB.
