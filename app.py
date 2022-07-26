import json

import requests
from flask import jsonify, make_response, Flask, request

from config import Config

app = Flask(__name__)
config = Config()

@app.route('/api/v1/weather/<string:language>/<float:latitude>/<float:longitude>')
def weatherLoc(language, latitude, longitude):
    dailyurl = f"https://weatherkit.apple.com/api/v1/weather/{language}/{latitude}/{longitude}"
    dataSets = request.args.get("dataSets")
    timezone = request.args.get("timezone")
    contryCode = request.args.get("countryCode")
    param = {
        "dataSets":dataSets,
        "timezone":timezone,
        "countryCode":contryCode
    }
    res = requests.get(dailyurl, headers={"Authorization": ("Bearer " + config.genToken())},params=param)
    res = json.loads(res.content)
    return make_response(jsonify(res))


if __name__ == '__main__':
    app.run(debug=True)
