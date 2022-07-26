import json
import requests
from flask import jsonify, make_response, Flask, request
from jwt_config import JwtConfig

app = Flask(__name__)
config = JwtConfig()


# 获取指定位置的天气数据 https://developer.apple.com/documentation/weatherkitrestapi/get_api_v1_weather_language_latitude_longitude
@app.route('/api/v1/weather/<string:language>/<float:latitude>/<float:longitude>', methods=['GET'])
def weatherLoc(language: str, latitude: float, longitude: float):
    url = f"https://weatherkit.apple.com/api/v1/weather/{language}/{latitude}/{longitude}"
    dataSets = request.args.get("dataSets")
    timezone = request.args.get("timezone")
    contryCode = request.args.get("countryCode")

    param = {
        "dataSets": dataSets,
        "timezone": timezone,
        "countryCode": contryCode
    }
    return __requestAndLoadJson(url, param)


# 确定可用于指定位置的数据集 https://developer.apple.com/documentation/weatherkitrestapi/get_api_v1_availability_latitude_longitude
@app.route("/api/v1/availability/<float:latitude>/<float:longitude>", methods=['GET'])
def availability(latitude: float, longitude: float):
    url = f"https://weatherkit.apple.com/api/v1/availability/{latitude}/{longitude}"
    country = request.args.get("country")
    param = {
        "country": country
    }
    return __requestAndLoadJson(url, param)


def __requestAndLoadJson(url, param: dict):
    res = requests.get(url, headers={"Authorization": ("Bearer " + config.genToken())}, params=param)
    res = json.loads(res.content)
    res = make_response(jsonify(res))
    return res


if __name__ == '__main__':
    app.run(debug=True)
