from . import app
from flask import redirect, request, abort
from . import models

standardResponse = {
    "status": None,
    "response": None,
    "messages": None
}
################################
# Basic Routes for Webpage bit #
################################
@app.route("/")
def index():
    pass

############################
# Authentication Endpoints #
############################
@app.route("/api/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        registrationResponse = standardResponse
        registrationJSON = request.get_json()
        email = registrationJSON.get("email")
        username = registrationJSON.get("username")
        password = registrationJSON.get("password")
        player = models.Player.objects(email=email).first()
        if player is not None:
            abort(409)
        player = models.Player.objects(username=username).first()
        if player is not None:
            abort(409)
        emailValid = True  # TODO: ADD Validation!
        usernameValid = True
        passwordValid = True
        if usernameValid:
            if emailValid:
                if passwordValid:
                    newPlayer = models.Player(username=username, email=email)
                    newPlayer.setPassword(password)
                    newPlayer.save()
                    registrationResponse["status"] = 200
                    registrationResponse["messages"] = ["Valid Email, Username, and Password, Account Created."]
                    return registrationResponse
                else:
                    abort(400)
            else:
                abort(400)
        else:
            abort(400)
    else:
        return "Currently only supports POST... this API is currently only accessible through PulseMan"


@app.route("/api/get_token", methods=["GET", "POST"])
def getToken():
    if request.method == "POST":
        tokenResponse = standardResponse
        tokenRequest = request.get_json()
        player = models.Player.objects(email=tokenRequest.get("email")).first()
        if player is None:
            abort(400)

        passwordValid = player.checkPassword(tokenRequest.get("password"))
        scopeValid = (tokenRequest.get("scope") in ["read", "write"])
        if passwordValid:
            if scopeValid:
                newToken = models.AuthToken(player=player, scope=tokenRequest.get("scope"))
                newToken.save()
                tokenResponse["status"] = 200
                tokenResponse["messages"] = ["Token Generated!"]
                tokenResponse["response"] = newToken.key
                return tokenResponse
            else:
                abort(400)
        else:
            abort(400)


######################
# MAP ENDPOINTS WEB #
######################
@app.route("/map")
def listMaps():
    return redirect("/map/list")


@app.route("/map/create")
def createMap():
    pass


@app.route("/map/view")
def viewMap():
    pass


@app.route("/map/edit")
def editMap():
    pass


@app.route("/map/delete")
def deleteMap():
    pass


@app.route("/map/list")
def listMap():
    pass


#########################
# Auto-Update Endpoints #
#########################
@app.route("/update")
def currentUpdate():
    updateData = {
        "version": "1.1.2",
        "changes": "Update Machine Broke",
        "directDL": "https://github.com/pulsarc/pulsarc/releases/kjkfhkjjhdfsjhdfskhdfskjkjdfss"
    }
    return updateData.to_json()


#################################
# API ENDPOINTS (Authenticated) #
#################################
@app.route("/api")
def apiInfo():
    return "This is the Pulserv API, used by the Pulserv client to interact, as well as PulseMan package manager."


# API Auth Token issue endpoint ~ Should be rate limited.
@app.route("/api/auth/token", methods=["GET, POST"])
def issueToken():
    username = request.args.get("username")
    password = request.args.get("password")
