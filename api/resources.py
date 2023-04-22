from flask_restful import Resource
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash
import config
from flask import request, jsonify
import requests

auth = HTTPBasicAuth()
users = config.users
api_key = config.WEATHER_API_KEY


@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


# This is example API Resource

class Weather(Resource):
    @auth.login_required
    def get(self):
        if request.args.get('city') is not None:
            city = request.args.get('city')
            url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
            response = requests.get(url)
            data = response.json()
            temp_c = data["current"]["temp_c"]
            humidity = data["current"]["humidity"]
            date = data["location"]["localtime"]
            # city = "Tehran"
            # temp_c = 21
            # humidity = 18
            # date = "2023-04-21 0:04"
            return jsonify({"Hum": humidity, "city": city, "Temp": temp_c, "date": date})
        else:
            return jsonify({"Msg": "Please insert city key in request"})

    def post(self):
        pass

    def delete(self):
        pass
