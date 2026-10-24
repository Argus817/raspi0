import time

class Key:
    MOD_LEFT_CONTROL = 0x01
    MOD_LEFT_SHIFT = 0x02
    MOD_LEFT_ALT = 0x04
    MOD_LEFT_GUI = 0x08  # win button
    MOD_RIGHT_CONTROL = 0x10
    MOD_RIGHT_SHIFT = 0x20
    MOD_RIGHT_ALT = 0x40
    MOD_RIGHT_GUI = 0x80  # win button

    KEY_RESERVED = 0x00
    KEY_ERROR_ROLLOVER = 0x01
    KEY_POST_FAIL = 0x02
    KEY_ERROR_UNDEFINED = 0x03
    KEY_A = 0x04
    KEY_B = 0x05
    KEY_C = 0x06
    KEY_D = 0x07  # Keyboard d and D
    KEY_E = 0x08  # Keyboard e and E
    KEY_F = 0x09  # Keyboard f and F
    KEY_G = 0x0A  # Keyboard g and G
    KEY_H = 0x0B  # Keyboard h and H
    KEY_I = 0x0C  # Keyboard i and I
    KEY_J = 0x0D  # Keyboard j and J
    KEY_K = 0x0E  # Keyboard k and K
    KEY_L = 0x0F  # Keyboard l and L
    KEY_M = 0x10  # Keyboard m and M
    KEY_N = 0x11  # Keyboard n and N
    KEY_O = 0x12  # Keyboard o and O
    KEY_P = 0x13  # Keyboard p and P
    KEY_Q = 0x14  # Keyboard q and Q
    KEY_R = 0x15  # Keyboard r and R
    KEY_S = 0x16  # Keyboard s and S
    KEY_T = 0x17  # Keyboard t and T
    KEY_U = 0x18  # Keyboard u and U
    KEY_V = 0x19  # Keyboard v and V
    KEY_W = 0x1A  # Keyboard w and W
    KEY_X = 0x1B  # Keyboard x and X
    KEY_Y = 0x1C  # Keyboard y and Y
    KEY_Z = 0x1D  # Keyboard z and Z

    KEY_1 = 0x1E  # Keyboard 1 and !
    KEY_2 = 0x1F  # Keyboard 2 and @
    KEY_3 = 0x20  # Keyboard 3 and #
    KEY_4 = 0x21  # Keyboard 4 and $
    KEY_5 = 0x22  # Keyboard 5 and %
    KEY_6 = 0x23  # Keyboard 6 and ^
    KEY_7 = 0x24  # Keyboard 7 and &
    KEY_8 = 0x25  # Keyboard 8 and *
    KEY_9 = 0x26  # Keyboard 9 and (
    KEY_0 = 0x27  # Keyboard 0 and )

    KEY_ENTER = 0x28  # Keyboard Return (ENTER)
    KEY_ESC = 0x29  # Keyboard ESCAPE
    KEY_BACKSPACE = 0x2A  # Keyboard DELETE (Backspace)
    KEY_TAB = 0x2B  # Keyboard Tab
    KEY_SPACE = 0x2C  # Keyboard Spacebar
    KEY_MINUS = 0x2D  # Keyboard - and _
    KEY_EQUAL = 0x2E  # Keyboard = and +
    KEY_LEFTBRACE = 0x2F  # Keyboard [ and {
    KEY_RIGHTBRACE = 0x30  # Keyboard ] and }
    KEY_BACKSLASH = 0x31  # Keyboard \ and |
    KEY_HASHTILDE = 0x32  # Keyboard Non-US # and ~
    KEY_SEMICOLON = 0x33  # Keyboard ; and :
    KEY_APOSTROPHE = 0x34  # Keyboard ' and "
    KEY_GRAVE = 0x35  # Keyboard ` and ~
    KEY_COMMA = 0x36  # Keyboard , and <
    KEY_DOT = 0x37  # Keyboard . and >
    KEY_SLASH = 0x38  # Keyboard / and ?
    KEY_CAPSLOCK = 0x39  # Keyboard Caps Lock

    KEY_F1 = 0x3A  # Keyboard F1
    KEY_F2 = 0x3B  # Keyboard F2
    KEY_F3 = 0x3C  # Keyboard F3
    KEY_F4 = 0x3D  # Keyboard F4
    KEY_F5 = 0x3E  # Keyboard F5
    KEY_F6 = 0x3F  # Keyboard F6
    KEY_F7 = 0x40  # Keyboard F7
    KEY_F8 = 0x41  # Keyboard F8
    KEY_F9 = 0x42  # Keyboard F9
    KEY_F10 = 0x43  # Keyboard F10
    KEY_F11 = 0x44  # Keyboard F11
    KEY_F12 = 0x45  # Keyboard F12

    KEY_SYSRQ = 0x46  # Keyboard Print Screen
    KEY_SCROLLLOCK = 0x47  # Keyboard Scroll Lock
    KEY_PAUSE = 0x48  # Keyboard Pause
    KEY_INSERT = 0x49  # Keyboard Insert
    KEY_HOME = 0x4A  # Keyboard Home
    KEY_PAGEUP = 0x4B  # Keyboard Page Up
    KEY_DELETE = 0x4C  # Keyboard Delete Forward
    KEY_END = 0x4D  # Keyboard End
    KEY_PAGEDOWN = 0x4E  # Keyboard Page Down
    KEY_RIGHT = 0x4F  # Keyboard Right Arrow
    KEY_LEFT = 0x50  # Keyboard Left Arrow
    KEY_DOWN = 0x51  # Keyboard Down Arrow
    KEY_UP = 0x52  # Keyboard Up Arrow

    KEY_NUMLOCK = 0x53  # Keyboard Num Lock and Clear
    KEY_KPSLASH = 0x54  # Keypad /
    KEY_KPASTERISK = 0x55  # Keypad *
    KEY_KPMINUS = 0x56  # Keypad -
    KEY_KPPLUS = 0x57  # Keypad +
    KEY_KPENTER = 0x58  # Keypad ENTER
    KEY_KP1 = 0x59  # Keypad 1 and End
    KEY_KP2 = 0x5A  # Keypad 2 and Down Arrow
    KEY_KP3 = 0x5B  # Keypad 3 and PageDn
    KEY_KP4 = 0x5C  # Keypad 4 and Left Arrow
    KEY_KP5 = 0x5D  # Keypad 5
    KEY_KP6 = 0x5E  # Keypad 6 and Right Arrow
    KEY_KP7 = 0x5F  # Keypad 7 and Home
    KEY_KP8 = 0x60  # Keypad 8 and Up Arrow
    KEY_KP9 = 0x61  # Keypad 9 and Page Up
    KEY_KP0 = 0x62  # Keypad 0 and Insert
    KEY_KPDOT = 0x63  # Keypad . and Delete

    KEY_102ND = 0x64  # Keyboard Non-US \ and |
    KEY_COMPOSE = 0x65  # Keyboard Application
    KEY_POWER = 0x66  # Keyboard Power
    KEY_KPEQUAL = 0x67  # Keypad =

    KEY_F13 = 0x68  # Keyboard F13
    KEY_F14 = 0x69  # Keyboard F14
    KEY_F15 = 0x6A  # Keyboard F15
    KEY_F16 = 0x6B  # Keyboard F16
    KEY_F17 = 0x6C  # Keyboard F17
    KEY_F18 = 0x6D  # Keyboard F18
    KEY_F19 = 0x6E  # Keyboard F19
    KEY_F20 = 0x6F  # Keyboard F20
    KEY_F21 = 0x70  # Keyboard F21
    KEY_F22 = 0x71  # Keyboard F22
    KEY_F23 = 0x72  # Keyboard F23
    KEY_F24 = 0x73  # Keyboard F24

    KEY_OPEN = 0x74  # Keyboard Execute
    KEY_HELP = 0x75  # Keyboard Help
    KEY_PROPS = 0x76  # Keyboard Menu
    KEY_FRONT = 0x77  # Keyboard Select
    KEY_STOP = 0x78  # Keyboard Stop
    KEY_AGAIN = 0x79  # Keyboard Again
    KEY_UNDO = 0x7A  # Keyboard Undo
    KEY_CUT = 0x7B  # Keyboard Cut
    KEY_COPY = 0x7C  # Keyboard Copy
    KEY_PASTE = 0x7D  # Keyboard Paste
    KEY_FIND = 0x7E  # Keyboard Find
    KEY_MUTE = 0x7F  # Keyboard Mute
    KEY_VOLUMEUP = 0x80  # Keyboard Volume Up
    KEY_VOLUMEDOWN = 0x81  # Keyboard Volume Down
    KEY_KPCOMMA = 0x85  # Keypad Comma
    KEY_RO = 0x87  # Keyboard International1
    KEY_KATAKANAHIRAGANA = 0x88  # Keyboard International2
    KEY_YEN = 0x89  # Keyboard International3
    KEY_HENKAN = 0x8A  # Keyboard International4
    KEY_MUHENKAN = 0x8B  # Keyboard International5
    KEY_KPJPCOMMA = 0x8C  # Keyboard International6
    KEY_HANGEUL = 0x90  # Keyboard LANG1
    KEY_HANJA = 0x91  # Keyboard LANG2
    KEY_KATAKANA = 0x92  # Keyboard LANG3
    KEY_HIRAGANA = 0x93  # Keyboard LANG4
    KEY_ZENKAKUHANKAKU = 0x94  # Keyboard LANG5

    KEY_KPLEFTPAREN = 0xB6  # Keypad (
    KEY_KPRIGHTPAREN = 0xB7  # Keypad )

    KEY_LEFTCTRL = 0xE0  # Keyboard Left Control
    KEY_LEFTSHIFT = 0xE1  # Keyboard Left Shift
    KEY_LEFTALT = 0xE2  # Keyboard Left Alt
    KEY_LEFTMETA = 0xE3  # Keyboard Left GUI
    KEY_RIGHTCTRL = 0xE4  # Keyboard Right Control
    KEY_RIGHTSHIFT = 0xE5  # Keyboard Right Shift
    KEY_RIGHTALT = 0xE6  # Keyboard Right Alt
    KEY_RIGHTMETA = 0xE7  # Keyboard Right GUI

    KEY_MEDIA_PLAYPAUSE = 0xE8
    KEY_MEDIA_STOPCD = 0xE9
    KEY_MEDIA_PREVIOUSSONG = 0xEA
    KEY_MEDIA_NEXTSONG = 0xEB
    KEY_MEDIA_EJECTCD = 0xEC
    KEY_MEDIA_VOLUMEUP = 0xED
    KEY_MEDIA_VOLUMEDOWN = 0xEE
    KEY_MEDIA_MUTE = 0xEF
    KEY_MEDIA_WWW = 0xF0
    KEY_MEDIA_BACK = 0xF1
    KEY_MEDIA_FORWARD = 0xF2
    KEY_MEDIA_STOP = 0xF3
    KEY_MEDIA_FIND = 0xF4
    KEY_MEDIA_SCROLLUP = 0xF5
    KEY_MEDIA_SCROLLDOWN = 0xF6
    KEY_MEDIA_EDIT = 0xF7
    KEY_MEDIA_SLEEP = 0xF8
    KEY_MEDIA_COFFEE = 0xF9
    KEY_MEDIA_REFRESH = 0xFA
    KEY_MEDIA_CALC = 0xFB


class Mouse:
    # Unique high-range identifiers for unified API routing
    LEFT = 0x1001
    RIGHT = 0x1002
    MIDDLE = 0x1003
    BACK = 0x1004
    FORWARD = 0x1005


def _write_gadget(path, report):
    try:
        with open(path, 'rb+') as fd:
            fd.write(report)
    except FileNotFoundError:
        print(f"[{path}] {report.hex()}")


def release_keys():
    """Resets the keyboard report to all zeros (all keys released)."""
    _write_gadget('/dev/hidg0', bytes([0] * 8))


def release_mouse():
    """Resets the mouse report to all zeros (all buttons and movement cleared)."""
    # 6 bytes total: [Report ID 1, buttons, x, y, wheel, padding][cite: 3]
    _write_gadget('/dev/hidg2', bytes([0x01, 0x00, 0x00, 0x00, 0x00, 0x00]))


def send_key(code, mod=0x00, release=True):
    """
    Unified API supporting both keyboard keys, modifier keys, and mouse buttons.
    - If `code` is a Mouse button, it performs a click action (press + release) on /dev/hidg2.
    - If `code` is a Modifier key (0xE0 - 0xE7), it automatically maps to the modifier byte.
    - If `code` is a Keyboard key, it sends the key report on /dev/hidg0.
    """
    if code in (Mouse.LEFT, Mouse.RIGHT, Mouse.MIDDLE, Mouse.BACK, Mouse.FORWARD):
        mouse_button_map = {
            Mouse.LEFT: 0x01,
            Mouse.RIGHT: 0x02,
            Mouse.MIDDLE: 0x04,
            Mouse.BACK: 0x08,
            Mouse.FORWARD: 0x10
        }
        btn_mask = mouse_button_map.get(code, 0x01)
        # Target /dev/hidg2 with Report ID 0x01[cite: 3]
        _write_gadget('/dev/hidg2', bytes([0x01, btn_mask, 0x00, 0x00, 0x00, 0x00]))
        if release:
            time.sleep(0.05)
            release_mouse()
    else:
        effective_mod = mod & 0xFF
        effective_key = code & 0xFF
        
        # Automatically handle modifier key codes passed directly as keys (0xE0 to 0xE7)
        if 0xE0 <= code <= 0xE7:
            effective_mod |= (1 << (code - 0xE0))
            effective_key = 0x00
            
        report = bytes([effective_mod, 0x00, effective_key, 0x00, 0x00, 0x00, 0x00, 0x00])
        _write_gadget('/dev/hidg0', report)
        if release:
            time.sleep(0.05)
            release_keys()


def send_keys(key1, key2=0x00, mod=0x00, release=True):
    """
    Sends two inputs simultaneously. Supports combinations of keyboard keys, 
    modifiers, and mouse buttons by dispatching them to their respective endpoints.
    """
    inputs = [key1, key2]
    
    # 1. Handle keyboard modifier if present
    effective_mod = mod & 0xFF
    kb_keys = []
    mouse_actions = []

    for k in inputs:
        if k == 0x00:
            continue
        if k in (Mouse.LEFT, Mouse.RIGHT, Mouse.MIDDLE, Mouse.BACK, Mouse.FORWARD):
            mouse_actions.append(k)
        elif 0xE0 <= k <= 0xE7:
            effective_mod |= (1 << (k - 0xE0))
        else:
            kb_keys.append(k & 0xFF)

    # 2. Dispatch Mouse Actions if any are in the mix
    if mouse_actions:
        # Determine combined button mask for mouse actions
        mouse_map = {
            Mouse.LEFT: 0x01, Mouse.RIGHT: 0x02, 
            Mouse.MIDDLE: 0x04, Mouse.BACK: 0x08, Mouse.FORWARD: 0x10
        }
        btn_mask = sum(mouse_map.get(m, 0) for m in mouse_actions)
        _write_gadget('/dev/hidg2', bytes([0x01, btn_mask, 0x00, 0x00, 0x00, 0x00]))

    # 3. Dispatch Keyboard Actions if any are present
    if kb_keys or effective_mod > 0:
        k1 = kb_keys[0] if len(kb_keys) > 0 else 0x00
        k2 = kb_keys[1] if len(kb_keys) > 1 else 0x00
        report = bytes([effective_mod, 0x00, k1, k2, 0x00, 0x00, 0x00, 0x00])
        _write_gadget('/dev/hidg0', report)

    # 4. Release both endpoints if requested
    if release:
        time.sleep(0.05)
        if mouse_actions:
            release_mouse()
        if kb_keys or effective_mod > 0:
            release_keys()


def mouse_scroll(wheel):
    """Scrolls the vertical wheel (positive for up, negative for down)."""
    def to_signed(v):
        return v & 0xFF
    report = bytes([0x01, 0x00, 0x00, 0x00, to_signed(wheel), 0x00])
    _write_gadget('/dev/hidg2', report)
    time.sleep(0.05)
    release_mouse()