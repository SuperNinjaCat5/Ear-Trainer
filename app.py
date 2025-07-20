from flask import Flask, render_template, request, redirect, url_for, abort, jsonify
from web_quiz_game import get_random_note, get_note_name, get_random_freq
from flask_dance.contrib.github import make_github_blueprint, github
from dotenv import load_dotenv
import os
import json_controller

debug_mode = False

load_dotenv()

def debug_print(text):
    if debug_mode == True:
        print(text)

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "supersekrit")
app.config["GITHUB_OAUTH_CLIENT_ID"] = os.environ.get("GITHUB_OAUTH_CLIENT_ID")
app.config["GITHUB_OAUTH_CLIENT_SECRET"] = os.environ.get("GITHUB_OAUTH_CLIENT_SECRET")
github_bp = make_github_blueprint()
app.register_blueprint(github_bp, url_prefix="/login")

VALID_PAGES = ['home', 'Quiz_Game', 'Learn_Game', 'Leaderboard', 'Quiz_Game_Menu']

@app.route("/")
@app.route("/home")
def home():
    if not github.authorized:
        return redirect(url_for("github.login"))

    resp = github.get("/user")
    assert resp.ok
    username = resp.json()["login"]
    return render_template("home.html", username=username)


@app.route("/quiz_game_menu")
def display_quiz_menu():
    return redirect(url_for("show_page_Quiz_Game"))

@app.route("/learn_game_menu")
def display_learn_menu():
    return render_template("Learn_Game_Menu.html")

@app.route("/Learn_Game")
def route_to_menu():
    return redirect(url_for("display_learn_menu"))

@app.route("/submit", methods=["POST"])
def submit_game_choice():
    choice = request.form.get("user_input")
    if choice in VALID_PAGES:
        if choice == 'Quiz_Game':
            print("Picked show page select game")
            return redirect(url_for("show_page_select_game", page=f'{choice}_Menu'))
        elif choice == 'Learn_Game':
            return redirect(url_for("display_learn_menu"))
        else:
            return redirect(url_for("show_page_select_game", page=choice))
    else:
        abort(404)

@app.route("/submit_level_duration_quiz", methods=["POST"])
def submit_level_duration():
    level = request.form.get("level")
    duration = request.form.get("duration")
    return redirect(url_for("show_page_Quiz_Game", level=level, duration=duration))

@app.route("/Quiz_Game/<level>-<duration>")
def show_page_Quiz_Game(level, duration):
    highscore = request.args.get("highscore", "")
    message = request.args.get("message", "")
    score = int(request.args.get("score", 0))
    freq = get_random_freq(level)
    duration_ms = 4000
    duration = float(duration)
    failpass = request.args.get("failpass", "")
    if duration == 0.5:
        duration_ms = 250
    if duration == 1:
        duration_ms = 500
    if duration == 2:
        duration_ms = 100
    if duration == 4:
        duration_ms = 2000
    
    if failpass:
        print("Is failpass")
        failpass = failpass
    else:
        failpass = "Pass"
    return render_template("Quiz_Game.html", level=level, duration=duration, freq=freq, score=score, message=message, duration_ms=duration_ms, failpass=failpass, highscore=highscore)

@app.route("/guess_submit_quiz_game", methods=["POST"])
def guess_submit_quiz_game():
    # Collect form data
    highscore = request.args.get("highscore", "")
    player_guess = request.form.get("player_guess")
    original_freq = float(request.form.get("original_freq"))
    level = request.form.get("level")
    duration = request.form.get("duration")
    score = int(request.form.get("score", 0))

    from web_quiz_game import get_random_freq

    note_freqs = {
        'C1': 32.70, 'C#1': 34.65, 'D1': 36.71, 'D#1': 38.89, 'E1': 41.20, 'F1': 43.65, 'F#1': 46.25, 'G1': 49.00, 'G#1': 51.91, 'A1': 55.00, 'A#1': 58.27, 'B1': 61.74,
        'C2': 65.41, 'C#2': 69.30, 'D2': 73.42, 'D#2': 77.78, 'E2': 82.41, 'F2': 87.31, 'F#2': 92.50, 'G2': 98.00, 'G#2': 103.83, 'A2': 110.00, 'A#2': 116.54, 'B2': 123.47,
        'C3': 130.81, 'C#3': 138.59, 'D3': 146.83, 'D#3': 155.56, 'E3': 164.81, 'F3': 174.61, 'F#3': 185.00, 'G3': 196.00, 'G#3': 207.65, 'A3': 220.00, 'A#3': 233.08, 'B3': 246.94,
        'C4': 261.63, 'C#4': 277.18, 'D4': 293.66, 'D#4': 311.13, 'E4': 329.63, 'F4': 349.23, 'F#4': 369.99, 'G4': 392.00, 'G#4': 415.30, 'A4': 440.00, 'A#4': 466.16, 'B4': 493.88
    }

    original_name = None
    for note, freq in note_freqs.items():
        if abs(freq - original_freq) < 0.01:
            original_name = note
            break
    if original_name is None:
        original_name = 'A4' 

    if player_guess.strip().upper() == original_name.upper():
        score += 1
        message = "Correct!"
        failpass = "Pass"
    else:
        message = f"Wrong Note! The correct note was {original_name}. You guessed: {player_guess.strip().upper()}"
        failpass = "Fail"

    resp = github.get("/user")
    if not resp.ok:
        return f"Failed to fetch user info: {resp.text}", 500
    user_data = resp.json()
    username = user_data.get("login")
    leaderboard_data = json_controller.read_data_json("leaderboard.json")

    return redirect(url_for("submit_leaderboard", level=level, duration=duration, score=score, message=message, failpass=failpass, highscore=highscore))
    #return redirect(url_for("show_page_Quiz_Game", level=level, duration=duration, score=score, message=message, failpass=failpass, highscore=data.get("score")))

@app.route("/<page>")
def show_page_select_game(page):
    if page in VALID_PAGES:
        return render_template(f"{page}.html")
    else:
        abort(404)

@app.route("/Learn_Game/<level>-<duration>")
def show_learn_game(level, duration):
    score = int(request.args.get("score", 0))
    freq = get_random_freq(level)
    duration_ms = 4000
    duration = float(duration)
    if duration == 0.5:
        duration_ms = 250
    if duration == 1:
        duration_ms = 500
    if duration == 2:
        duration_ms = 1000
    if duration == 4:
        duration_ms = 2000

    note_name = get_note_name(level, freq)

    return render_template("Learn_Game.html", level=level, duration=duration, freq=freq, score=score, duration_ms=duration_ms, note_name=note_name)

@app.route("/submit_level_duration_learn", methods=["POST"])
def submit_level_duration_learn():
    level = request.form.get("level")
    duration = request.form.get("duration")
    return redirect(url_for("show_learn_game", level=level, duration=duration))

@app.route("/Submit_Leaderboard", methods=["GET", "POST"])
def submit_leaderboard():
    highscore = request.args.get("highscore", "")
    level = request.args.get("level")
    duration = request.args.get("duration") 
    score = request.args.get("score")
    message = request.args.get("message", "")
    failpass = request.args.get("failpass", "")
    score = request.args.get("score")

    if not github.authorized:
        return jsonify({"error": "Unauthorized"}), 401

    resp = github.get("/user")
    if not resp.ok:
        return jsonify({"error": f"Failed to fetch user info: {resp.text}"}), 500
    
    user_data = resp.json()
    
    data = {
        "username": user_data.get("login"),
        "score": score
    }
    debug_print(f" Data {user_data}")

    json_controller.write_data_json("leaderboard.json", data)

    leaderboard_data = json_controller.read_data_json("leaderboard.json")
    player_data = leaderboard_data.get(user_data.get("login"))
    highscore=player_data.get("scores")
    highscore = max(highscore) if highscore else 0

    debug_print(highscore)

    highscore = int(highscore) if highscore and isinstance(highscore, (int, float)) else 0
    score = int(score) if score and score.isdigit() else 0
    return redirect(url_for("show_page_Quiz_Game", level=level, duration=duration, score=score, message=message, failpass=failpass, highscore=highscore))

@app.route("/Leaderboard")
def show_leaderboard():
    resp = github.get("/user")
    if not resp.ok:
        return f"Failed to fetch user info: {resp.text}", 500
    user_data = resp.json()
    current_username = user_data.get("login")
    leaderboard_data = json_controller.read_data_json("leaderboard.json")
    current_user_data = leaderboard_data.get(current_username)

    current_user_highscore=current_user_data.get("scores")
    current_user_highscore = max(current_user_highscore) if current_user_highscore else 0
    data_to_pass = {} 
    for player in leaderboard_data:
        loop_player_data = leaderboard_data.get(player)
        loop_current_user_score = loop_player_data.get("scores")
        loop_current_user_highscore = max(loop_current_user_score) if loop_current_user_score else 0
        data_to_pass[player] = loop_current_user_highscore

    debug_print(data_to_pass)
    return render_template("Leaderboard.html", data=data_to_pass)

if __name__ == "__main__":
    debug_mode = True
    app.run(ssl_context='adhoc', host="127.0.0.1", port=5000, debug=True)