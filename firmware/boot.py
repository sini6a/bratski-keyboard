import board

from kmk.bootcfg import bootcfg

bootcfg(
    sense=board.GP6,  # column
    source=board.GP3,  # row
    midi=False,
    mouse=False,
    storage=False,
    usb_id=('Sinisha Stojchevski', 'Bratski Keyboard'),
)
