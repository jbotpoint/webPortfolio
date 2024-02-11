from flask import Blueprint
from flask import Flask, render_template, url_for, request

import json

from package import handleAPIs

bp = Blueprint("pages", __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/about")
def about():
    return render_template("about.html")

@bp.route("/notesandlinks")
def notesandlinks():
    return render_template("notesandlinks.html")

@bp.route("/matlas")
def matlas():
    return render_template("mappingProject.html")

@bp.route("/weather", methods=['POST', 'GET'])
def weather():
    if request.method == "POST":
        cityName = request.form["city"]
        response = handleAPIs.getWeather(cityName)
        if(response != False):
            responseList = [response['current']['temp_c'], response['current']['condition']['text'], response['current']['condition']['code']]
            return render_template("weatherExtends.html", title=cityName, currentTemp=responseList[0], condition=responseList[1], conditionCode=responseList[2])
    return render_template("weather.html", title="Weather")