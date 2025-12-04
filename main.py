import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC

keyboard = KMKKeyboard()

PINS = [board.D3, board.D4, board.D2, board.D1]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [KC.P8, KC.P4, KC.P5, KC.P6]
]

if __name__ == '__main__':
    keyboard.go()
