from flask import Flask
from flask import render_template
from flask import jsonify
import requests

app = Flask(__name__)

@app.route("/")
def weather():
    city = "London"
    apikey = "a6311858fb35df63b55216bae4aa952a"
    url = "http://api.openweathermap.org/data/2.5/weather?appid=" + apikey + "&q=" + city
    request = requests.get(url)
    response = request.json()
    weather = response["weather"]
    details = response["main"]
    description = weather[0]["description"]
    temperature = details["temp"]
    feels_like = details["feels_like"]
    temp_min = details["temp_min"]
    temp_max = details["temp_max"]
    humidity = details["humidity"]
    pressure = details["pressure"]
    status_code = request.status_code
    return render_template(
            "weather.html",
            weather = description,
            temperature = temperature,
            feels_like = feels_like,
            temp_min = temp_min,
            temp_max = temp_max,
            humidity = humidity,
            pressure = pressure,
            status_code = status_code
        )


@app.route("/ping")
def ping():
    return render_template("ping-pong.html")

@app.route("/health")
def health():
    responce = {
        "Responce": "HEALTHY",
        "Status": "200 OK"
    }
    return jsonify(responce)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host = "0.0.0.0", port = 8080)
