from flask import Flask, jsonify
import json

app = Flask(__name__)

def get_players_leaderboard():
    with open("leaderboard.json") as json_file:
        data = json.load(json_file)
    return data


@app.route("/", methods=['GET'])
def hello_world():
    return "It works"

@app.route("/leaderboard", methods=['GET'])
def leaderboard():
    leaderboard = get_players_leaderboard()
    return jsonify(leaderboard)