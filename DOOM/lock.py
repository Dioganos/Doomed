import keyboard
import mouse
import os

fareyiKilitle = True

#klavye kilitleme
def KlavyeyiKilitle():
    engellenecekTuslar = {'alt','tab','right arrow','left arrow','up arrow','down arrow','escape','delete','backspace', 'alt gr', 'ctrl', 'left alt', 'left ctrl', 'left shift', 'left windows', 'right alt', 'right ctrl', 'right shift', 'right windows', 'shift', 'windows'}
    for herBirTus in engellenecekTuslar:
        keyboard.block_key(herBirTus)
KlavyeyiKilitle()

def kapat():
    keyboard.unhook_all()
    global fareyiKilitle
    fareyiKilitle = False

#programı kapatmak için şifre hesoyam yazıp space ya da enter basılması
keyboard.add_word_listener('hesoyam', kapat, triggers=['space', 'enter'], match_suffix=True, timeout=3)

#programın kapanma şartı ve mouse kilitleme
while (fareyiKilitle):
    mouse.move(0,0, absolute=True, duration=0)