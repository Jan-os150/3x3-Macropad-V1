print("Starting")

#Imports
import board
from kmk.extensions.media_keys import MediaKeys
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Macros, Press, Release, Tap, Delay
from kmk.modules.layers import Layers


#Modules
keyboard = KMKKeyboard()
macros = Macros()


keyboard.col_pins = (board.D4, board.D3, board.D2)
keyboard.row_pins = (board.D7, board.D6, board.D5)
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(macros)
keyboard.modules.append(Layers())

#Macros -------------------------------------------------------------------------------------------
Disc = KC.MACRO(
    Press(KC.RCTRL),
    Tap(KC.M),
    Release(KC.RCTRL)
)

#Open Lightroom
lightRoom = KC.MACRO(
    Press(KC.LWIN),
    Tap(KC.R),
    Release(KC.LWIN),
    r'C:\Program Files\Adobe\Adobe Lightroom Classic\Lightroom.exe',
    Tap(KC.ENT)
)

#CMD as Admin
cmdAdmin = KC.MACRO(
    Press(KC.LWIN),
    Tap(KC.X),
    Release(KC.LWIN),
    Delay(50),
    Tap(KC.A),
    Tap(KC.ENT)
)

#Hide all
hide = KC.MACRO(
    Press(KC.LWIN),
    Tap(KC.D),
    Release(KC.LWIN)
)

#Print Screen
prnt = KC.MACRO( 
    Press(KC.LCTRL),
    Tap(KC.PSCR),
    Release(KC.LCTRL)
)


#Force Quit
forceQuit = KC.MACRO(
    Press(KC.LALT),
    Tap(KC.F4),
    Release(KC.LALT)
)

#Gamebar
gameBar = KC.MACRO(
    Press(KC.LWIN),
    Tap(KC.G),
    Release(KC.LWIN)
)

#Move next virtual desktop
MNVD = KC.MACRO(
    Press(KC.LCTRL),
    Delay(50),
    Press(KC.LWIN),
    Tap(KC.RIGHT),
    Delay(50),
    Release(KC.LCTRL),
    Delay(50),
    Release(KC.LWIN)
    
)

#Move previous virtual desktop
MPVD = KC.MACRO(
    Press(KC.LCTRL),
    Delay(50),
    Press(KC.LWIN),
    Tap(KC.LEFT),
    Delay(50),
    Release(KC.LCTRL),
    Delay(50),
    Release(KC.LWIN)
    
)
#--------------------------------------------------------------------------------------------------



#Layers
TRANS = KC.TRNS
Switch = KC.TG(1)

#Keymap
keyboard.keymap = [
    
    #Base Layer
    [
        Switch, Disc, lightRoom, 
        KC.MPLY, KC.MPRV, KC.MNXT, 
        gameBar, hide, forceQuit 
    ],
    
    #Work Layer
    [
        TRANS, Disc, cmdAdmin, 
        KC.MUTE, MPVD, MNVD, 
        prnt, hide, forceQuit 
    ]
]

if __name__ == '__main__':
    keyboard.go()
