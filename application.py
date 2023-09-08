# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Api, abort, reqparse

from sudokuApiHandler import (
    input_check,
    sodoku_board_handler,
    sodoku_full_game_handler,
    sodoku_solvable_handler,
)

# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)


def check_if_full_board(x):
    if not input_check(x):
        abort("This not an valid value!")


@app.route("/api/fullgame", methods=["GET"])
def full_game():
    res = sodoku_full_game_handler()
    return jsonify(res["message"]), res["status_code"]


@app.route("/api/makeboard", methods=["GET"])
def make_board():
    res = sodoku_board_handler()
    return jsonify(res["message"]), res["status_code"]


@app.route("/api/solver", methods=["POST"])
def solver():
    data = request.get_json()
    print(data)
    if not input_check(data["value"]):
        return jsonify("This not an valid value!"), 400
    res = sodoku_solvable_handler(data["value"])
    return jsonify(res["message"]), res["status_code"]


# driver function
if __name__ == "__main__":
    app.run(debug=True)
