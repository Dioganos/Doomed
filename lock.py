import keyboard
import mouse
import shutil
import os

"""BizimDosyaAdiExeUzantili = "lock.exe"


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


#Başlangıçta çalıştırma muhabbeti
hedefKonum = os.path.expanduser('~/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup')
oradaMi = hedefKonum + "/" + BizimDosyaAdiExeUzantili

aramaSonucu = find(BizimDosyaAdiExeUzantili, "C:")

if(aramaSonucu != None):
    if not os.path.isfile(oradaMi):
        shutil.move(os.path.join(aramaSonucu), hedefKonum)
else:
    aramaSonucu = find(BizimDosyaAdiExeUzantili, "D:")
    if not os.path.isfile(oradaMi):
        shutil.move(os.path.join(aramaSonucu), hedefKonum)
"""


#klavye kilitleme
calisiyor = True
a = {'alt', 'alt gr', 'ctrl', 'left alt', 'left ctrl', 'left shift', 'left windows', 'right alt', 'right ctrl', 'right shift', 'right windows', 'shift', 'windows'}
for x in a:
    keyboard.block_key(x)

def kapat():
    keyboard.unhook_all()
    global calisiyor
    calisiyor = False

#programı kapatmak için şifre hesoyam yazıp space ya da enter basılması
keyboard.add_word_listener('hesoyam', kapat, triggers=['space', 'enter'], match_suffix=True, timeout=3)

#programın kapanma şartı ve mouse kilitleme
while (calisiyor):
    mouse.move(0,0, absolute=True, duration=0)