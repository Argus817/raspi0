from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
from datetime import timedelta
from keyboard import Keycodes, send_key
import json
import time

app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = timedelta(days=30)

socketio = SocketIO(app, cors_allowed_origins="*", async_mode="threading")

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

def load_data():
    with open("spells.json", "r") as f:
        return json.load(f)

def save_data(data):
    with open("spells.json", "w") as f:
        json.dump(data, f, indent=4, sort_keys=False)

@app.route("/")
def index():
    data = load_data()
    return render_template(
        "index.html",
        all_spells=data["all_spells"],
        spell_sets=data["spell_sets"]
    )

@app.route("/edit")
def edit():
    data = json.load(open("spells.json"))
    return render_template(
        "edit.html",
        all_spells=data["all_spells"],
        spell_sets=data["spell_sets"],
        spell_order=data.get("spell_order", list(data["all_spells"].keys()))
    )



@app.route("/save-layout", methods=["POST"])
def save_layout():
    data = request.get_json()
    # Preserve order using spell_order from client
    with open("spells.json", "w") as f:
        json.dump(data, f, indent=4, sort_keys=False)
    return "ok"


@socketio.on("cast")
def handle_cast(data):
    spellset = data.get("spellset")
    slot = data.get("slot")

    game = load_data()
    spell_sets = game["spell_sets"]

    if spellset not in spell_sets:
        return
    if slot not in spell_sets[spellset]:
        return

    send_key(SpellSetKey[spellset])
    time.sleep(0.04)
    send_key(SlotKey[slot])

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)

