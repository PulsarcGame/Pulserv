from . import app
from flask import redirect
from . import models

################################
# Basic Routes for Webpage bit #
################################
@app.route("/")
def index():
    pass

#################
# MAP ENDPOINTS #
#################
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
