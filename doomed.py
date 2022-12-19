import first
from threading import Thread
import os


def Yazilar():
    first.kafatasiSekmesi()
    for i in range(0, 29):
        Thread(target= first.aciklamaSekmesi).start()
    first.sonSekme()
    os.system('python main.py')


def Lock():
    exec("import lock")

Thread(target=Lock).start()
Thread(target=Yazilar).start()
