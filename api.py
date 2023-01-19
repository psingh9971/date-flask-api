from flask import Flask
from dateApi.controller import date_api

api = Flask(__name__)
api.register_blueprint(date_api)


@api.route("/")
def test_service():
    return "ok"


if __name__ == "__main__":
    api.run(host="localhost", port=8080)