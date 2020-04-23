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
```

## More Details:

The server will communicate with the client over a semi-RESTful API design, the client will request a token from the server using login details, password and username cannot be used aside from initial token request.

The server itself will store Map files in raw binary, packaged into .psm archives (a renamed zip)

There will be three major platforms supported by the server
  - Online, browsable catalog (Highest Priority)
  - Ingame, API powered catalog (Still high priority)
  - PulseMan, A package manager, used for development, testing, and potentially baked into the PulseArc game.
  
 
