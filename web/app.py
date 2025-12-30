from flask import Flask, render_template
from flask_socketio import SocketIO
from datetime import timedelta
from keyboard import Keycodes, send_key
import json

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = timedelta(seconds=1)

SpellSetKey = {
    "1": Keycodes.KEY_F1,
    "2": Keycodes.KEY_F2,
    "3": Keycodes.KEY_F3,
    "4": Keycodes.KEY_F4,
}

SlotKey = {
    "1": Keycodes.KEY_1,
    "2": Keycodes.KEY_2,
    "3": Keycodes.KEY_3,
    "4": Keycodes.KEY_4,
}

def load_spells():
    with open("spells.json", "r") as f:
        data = json.load(f)["spell_sets"]
        return data

@app.route("/")
def index():
    # HTTP is used ONLY to fetch config / render UI
    spells = load_spells()
    return render_template("index.html", spells=spells)

@socketio.on("cast")
def handle_cast(data):
    """
    data = {
      spellset: "1",
      slot: "top"
    }
    """
    spellset = data["spellset"]
    slot = data["slot"]

    # Hooked keystroke logic here
    print(f"[WS] Cast → SpellSet {spellset}, Slot {slot}")
    send_key(SpellSetKey[spellset])
    send_key(SlotKey[slot])

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
