from . import app

standardResponse = {
    "status": None,
    "response": None,
    "messages": None
}
############################
# Authentication Endpoints #
############################
@app.route("/v1/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        registrationResponse = standardResponse
        registrationJSON = request.get_json()
        email = registrationJSON.get("email")
        username = registrationJSON.get("username")
        password = registrationJSON.get("password")
        player = database.models.Player.objects(email=email).first()
        if player is not None:
            abort(409)
        player = database.models.Player.objects(username=username).first()
        if player is not None:
            abort(409)
        emailValid = True  # TODO: ADD Validation!
        usernameValid = True
        passwordValid = True
        if usernameValid:
            if emailValid:
                if passwordValid:
                    newPlayer = database.models.Player(username=username, email=email)
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


@app.route("/v1/get_token", methods=["GET", "POST"])
def getToken():
    if request.method == "POST":
        tokenResponse = standardResponse
        tokenRequest = request.get_json()
        player = database.models.Player.objects(email=tokenRequest.get("email")).first()
        if player is None:
            abort(400)

        passwordValid = player.checkPassword(tokenRequest.get("password"))
        scopeValid = (tokenRequest.get("scope") in ["read", "write"])
        if passwordValid:
            if scopeValid:
                newToken = database.models.AuthToken(player=player, scope=tokenRequest.get("scope"))
                newToken.save()
                tokenResponse["status"] = 200
                tokenResponse["messages"] = ["Token Generated!"]
                tokenResponse["response"] = newToken.key
                return tokenResponse
            else:
                abort(400)
        else:
            abort(400)
