from flask import Flask, jsonify, request
import json

app = Flask(__name__)

def get_players_leaderboard() -> dict:
    with open("leaderboard.json") as json_file:
        data = json.load(json_file)
    return data

def update_leaderboard(game) -> dict:
    leaderboard = get_players_leaderboard()
    players_list = []
    new_leaderboard = {}
    status = {}

    for key, value in leaderboard.items():
        players_list.append(value)
    players_list.append(game)
    players_list.sort( key=lambda x: x['points'], reverse=True)
    for x in range(10):
        new_leaderboard[x] = players_list[x]
    
    with open("leaderboard.json", 'w') as json_file:
        json.dump(new_leaderboard, json_file, indent=4)

    if players_list[10] == game:
        status['status'] = 'ok'
        status['msg'] = 'You didn\'t make it'
    else:
        status['status'] = 'ok'
        status['msg'] = 'You made the top 10!'
    
    return status


@app.route("/", methods=['GET'])
def hello_world():
    return "It works"

@app.route("/leaderboard", methods=['GET'])
def leaderboard():
    leaderboard = get_players_leaderboard()
    return jsonify(leaderboard)

@app.route("/submit_score", methods=['POST'])
def submit_score():
    name = request.json.get('name')
    points = request.json.get('points')
    if not name or not points:
        return jsonify({"status": "error", "reason":"No name or points"})
    # TODO SANITIZE THE DATA
    output = update_leaderboard({"name": name, "points": points})
    return jsonify(output)