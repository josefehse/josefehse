import json
import os
import secrets
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

DATA_FILE = os.path.join(os.path.dirname(__file__), "jam_list.json")


def load_jam():
    """Load the jam list from the JSON file."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            return []
    return []


def save_jam(jam):
    """Persist the jam list to the JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(jam, f, indent=2, ensure_ascii=False)


@app.route("/")
def index():
    jam = load_jam()
    return render_template("index.html", jam=jam)


@app.route("/join", methods=["POST"])
def join():
    name = request.form.get("name", "").strip()
    song1 = request.form.get("song1", "").strip()
    song2 = request.form.get("song2", "").strip()

    if not name or not song1:
        # Required fields missing — bounce back with an error flag
        jam = load_jam()
        return render_template("index.html", jam=jam, error="Name and at least one song are required.")

    token = secrets.token_urlsafe(16)
    songs = [song1]
    if song2:
        songs.append(song2)

    jam = load_jam()
    jam.append({"name": name, "songs": songs, "token": token})
    save_jam(jam)
    return redirect(url_for("index"))


@app.route("/remove/<token>", methods=["POST"])
def remove(token):
    jam = load_jam()
    jam = [entry for entry in jam if entry.get("token") != token]
    save_jam(jam)
    return redirect(url_for("index"))


if __name__ == "__main__":
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    app.run(debug=debug)
