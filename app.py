from flask import Flask, render_template, request, redirect, url_for, abort
from web_quiz_game import get_random_note, get_note_name, get_random_freq
app = Flask(__name__)

VALID_PAGES = ['home', 'Quiz_Game', 'Learn_Game', 'Leaderboard', 'Quiz_Game_Menu']

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/submit", methods=["POST"])
def submit_game_choice():
    choice = request.form.get("user_input")
    if choice in VALID_PAGES:
        return redirect(url_for("show_page_select_game", page=f'{choice}_Menu'))
    else:
        abort(404)

@app.route("/submit_level_duration", methods=["POST"])
def submit_level_duration():
    level = request.form.get("level")
    duration = request.form.get("duration")
    return redirect(url_for("show_page_Quiz_Game", level=level, duration=duration))

@app.route("/Quiz_Game/<level>-<duration>")
def show_page_Quiz_Game(level, duration):
    freq = get_random_freq(level)
    score = int(request.args.get("score", 0))  # default score = 0
    return render_template("Quiz_Game.html", level=level, duration=duration, freq=freq, score=score)

@app.route("/guess_submit_quiz_game", methods=["POST"])
def guess_submit_quiz_game():
    # Collect form data
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

    new_freq = get_random_freq(level)

    return redirect(url_for("show_page_Quiz_Game", level=level, duration=duration, score=score))

@app.route("/<page>")
def show_page_select_game(page):
    if page in VALID_PAGES:
        return render_template(f"{page}.html")
    else:
        abort(404)

if __name__ == "__main__":
    app.run(debug=True)
