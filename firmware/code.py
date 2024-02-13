
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.tapdance import TapDance

print("Starting")

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())
tapdance = TapDance()
tapdance.tap_time = 65
keyboard.modules.append(tapdance)


keyboard.col_pins = (board.GP6,
                     board.GP7,
                     board.GP8,
                     board.GP9,
                     board.GP15,
                     board.GP14,
                     board.GP13,
                     board.GP12,
                     board.GP19,
                     board.GP20,
                     board.GP21,
                     board.GP28)
keyboard.row_pins = (board.GP3,
                     board.GP2,
                     board.GP1,
                     board.GP0)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.NO, KC.Q, KC.W,KC.E,KC.R,KC.T,KC.Y,KC.U,KC.I,KC.O,KC.P,KC.BKDL,
        KC.TAB, KC.A,KC.S,KC.D,KC.F,KC.G,KC.H,KC.J,KC.K,KC.L,KC.SCLN, KC.ENTER,
        KC.LSFT, KC.Z,KC.X,KC.C,KC.V,KC.B,KC.N,KC.M,KC.COMM,KC.DOT,KC.SLSH,KC.RSFT,
        KC.LCTL,KC.LGUI,KC.NO,KC.MO(1),KC.NO,KC.SPACE,KC.NO,KC.RALT,KC.NO,KC.FN,KC.RCTL,
     ],
     [
        KC.ESC,KC.N1,KC.N2,KC.N3,KC.N4,KC.N5,KC.N6,KC.N7,KC.N8,KC.N9,KC.N0,KC.BKDL,
        KC.NO,KC.F1,KC.F2,KC.F3,KC.F4,KC.F5,KC.F6,KC.F7,KC.F8,KC.F9,KC.F10,KC.NO,
        KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,
        KC.NO,KC.LGUI,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.LEFT,KC.NO,KC.UP,KC.DOWN,KC.RIGHT,
     ],
]

#,KC.LBRC
#KC.QUOT,

if __name__ == '__main__':
    keyboard.go()
