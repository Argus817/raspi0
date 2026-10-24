from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
from datetime import timedelta
from keyboard import Key, Mouse, send_key, send_keys
import json
import time
import threading

app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = timedelta(days=30)

socketio = SocketIO(app, cors_allowed_origins="*", async_mode="threading")

############ GOW3 ########################################

# --- USB HID Keycode Mappings ---
# Adjust these scancodes to match your emulator (e.g., RPCS3) keyboard configuration:
KEY_CROSS = Key.KEY_SPACE
KEY_CIRCLE = Key.KEY_LEFTSHIFT
KEY_SQUARE = Mouse.LEFT
KEY_TRIANGLE = Mouse.RIGHT


# --- God of War III Giant Harp Sequence (Rhythmic Timings) ---
# Structured as: (key1, key2, delay_after_seconds)
HARP_SEQUENCE = [
    # --- Phrase 1: X, X, X, CIRCLE (Steady moderate tempo) ---
    (KEY_CROSS, 0x00, 1),
    (KEY_CROSS, 0x00, 1),
    (KEY_CROSS, 0x00, 1),
    (KEY_CIRCLE, 0x00, 0.90), # Brief pause at end of phrase
    
    # --- Phrase 2: SQUARE, CIRCLE, SQUARE, X, TRIANGLE ---
    (KEY_SQUARE, 0x00, 0.55),
    (KEY_CIRCLE, 0x00, 0.55),
    (KEY_SQUARE, 0x00, 0.55),
    (KEY_CROSS, 0x00, 0.55),
    (KEY_TRIANGLE, 0x00, 0.90),
    
    # --- Phrase 3: SQUARE, CIRCLE, TRIANGLE, SQUARE + X ---
    (KEY_SQUARE, 0x00, 0.55),
    (KEY_CIRCLE, 0x00, 0.55),
    (KEY_TRIANGLE, 0x00, 0.55),
    (KEY_SQUARE, KEY_CROSS, 0.90), # Simultaneous chord
    
    # --- Phrase 4: SQUARE, TRIANGLE, SQUARE + X, TRIANGLE, TRIANGLE + CIRCLE ---
    (KEY_SQUARE, 0x00, 0.55),
    (KEY_TRIANGLE, 0x00, 0.55),
    (KEY_SQUARE, KEY_CROSS, 0.55), 
    (KEY_TRIANGLE, 0x00, 0.55),
    (KEY_TRIANGLE, KEY_CIRCLE, 0.90), 
    
    # --- Phrase 5: TRIANGLE + CIRCLE, X, SQUARE, SQUARE + X, CIRCLE, TRIANGLE, TRIANGLE + CIRCLE ---
    (KEY_TRIANGLE, KEY_CIRCLE, 0.55), 
    (KEY_CROSS, 0x00, 0.55),
    (KEY_SQUARE, 0x00, 0.55),
    (KEY_SQUARE, KEY_CROSS, 0.55), 
    (KEY_CIRCLE, 0x00, 0.55),
    (KEY_TRIANGLE, 0x00, 0.55),
    (KEY_TRIANGLE, KEY_CIRCLE, 0.75)  # Final note execution
]

# Threading control
harp_thread = None
stop_event = threading.Event()

# Map key codes to human-readable labels for the UI
KEY_NAMES = {
    KEY_CROSS: 'Cross (X)',
    KEY_CIRCLE: 'Circle',
    KEY_SQUARE: 'Square',
    KEY_TRIANGLE: 'Triangle'
}

def get_key_name(k1, k2):
    name1 = KEY_NAMES.get(k1, f"0x{k1:02X}")
    if k2 != 0x00:
        name2 = KEY_NAMES.get(k2, f"0x{k2:02X}")
        return f"{name1} + {name2}"
    return name1

def run_harp_puzzle(socketio_instance):
    stop_event.clear()
    socketio_instance.emit('gow3: status', {'status': 'running', 'message': 'Starting harp sequence...'})
    
    for idx, (k1, k2, delay) in enumerate(HARP_SEQUENCE, 1):
        # Check if stop was requested
        if stop_event.is_set():
            socketio_instance.emit('gow3: status', {'status': 'stopped', 'message': 'Sequence stopped by user.'})
            break
            
        key_desc = get_key_name(k1, k2)
        
        # Broadcast current note progress to the browser
        socketio_instance.emit('gow3: update', {
            'index': idx, 
            'total': len(HARP_SEQUENCE), 
            'key': key_desc
        })
        
        # Send keypresses
        if k2 != 0x00:
            send_keys(k1, key2=k2, release=True)
        else:
            send_key(k1, release=True)
            
        time.sleep(delay)
    else:
        socketio_instance.emit('gow3: status', {'status': 'completed', 'message': 'Sequence completed successfully!'})

@app.route("/gow3")
def gow3_index():
    return render_template("gow3/index.html")

@socketio.on("gow3: playharp")
def handle_playharp(data):
    global harp_thread
    # Prevent starting a new thread if one is already running
    if harp_thread is None or not harp_thread.is_alive():
        harp_thread = threading.Thread(target=run_harp_puzzle, args=(socketio,))
        harp_thread.start()

@socketio.on("gow3: stopharp")
def handle_stopharp(data):
    stop_event.set() 

##########################################################

############ HOGWARTS LEGACY #############################

SpellSetKey = {
    "1": Key.KEY_F1,
    "2": Key.KEY_F2,
    "3": Key.KEY_F3,
    "4": Key.KEY_F4,
}

SlotKey = {
    "1": Key.KEY_1,
    "2": Key.KEY_2,
    "3": Key.KEY_3,
    "4": Key.KEY_4,
}

def load_hlspell_data():
    with open("templates/hogwarts-legacy/spells.json", "r") as f:
        return json.load(f)

def save_hlspell_data(data):
    with open("templates/hogwarts-legacy/spells.json", "w") as f:
        json.dump(data, f, indent=4, sort_keys=False)

@app.route("/hogwarts-legacy")
def hl_index():
    data = load_hlspell_data()
    return render_template(
        "hogwarts-legacy/index.html",
        all_spells=data["all_spells"],
        spell_sets=data["spell_sets"]
    )

@app.route("/hogwarts-legacy/edit")
def hl_edit():
    data = load_hlspell_data() 
    return render_template(
        "hogwarts-legacy/edit.html",
        all_spells=data["all_spells"],
        spell_sets=data["spell_sets"],
        spell_order=data.get("spell_order", list(data["all_spells"].keys()))
    )



@app.route("/hogwarts-legacy/save-layout", methods=["POST"])
def hl_save_layout():
    data = request.get_json()
    # Preserve order using spell_order from client
    save_hlspell_data(data)
    return "ok"


@socketio.on("hogwarts-legacy: cast")
def hl_handle_cast(data):
    spellset = data.get("spellset")
    slot = data.get("slot")

    game = load_hlspell_data()
    spell_sets = game["spell_sets"]

    if spellset not in spell_sets:
        return
    if slot not in spell_sets[spellset]:
        return

    send_key(SpellSetKey[spellset])
    time.sleep(0.04)
    send_key(SlotKey[slot])

##########################################################

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)

