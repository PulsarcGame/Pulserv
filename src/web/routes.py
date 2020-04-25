from . import app, loginMan
from flask import redirect, request, render_template, flash, Markup
from flask_login import login_required
from ..mapProcessor import unpacker

################################
# Basic Routes for Webpage bit #
################################
@app.route("/")
def index():
    return render_template("index.html")


######################
# MAP ENDPOINTS WEB #
######################
@app.route("/map")
def listMaps():
    return redirect("/map/list")


@app.route("/map/upload", methods=["GET", "POST"])
def uploadMap():
    if request.method == "POST":
        uploadedMap = request.files["map"]
        MapPackage = unpacker.MapPackage(uploadedMap.read())
        print(MapPackage.raw)
        return str(MapPackage.raw)
    else:
        return render_template("upload.html")


@app.route("/map/view")
def viewMap():
    pass


@app.route("/map/edit")
@login_required
def editMap():
    pass


@app.route("/map/delete")
@login_required
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
