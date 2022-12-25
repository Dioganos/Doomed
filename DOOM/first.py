import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle
import random
import os
DOOM_konum = os.path.expanduser('~/Doomed/DOOM')

class ImageLabel(tk.Label):

    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []
        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass



        self.frames = cycle(frames)

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)


def otomatikYazi(widget, index, string):
    if len(string) > 0:
        widget.insert(index, string[0])
        if len(string) > 1:
            # compute index of next char
            index = widget.index("%s + 1 char" % index)

            # type the next character in half a second
            widget.after(70, otomatikYazi, widget, index, string[1:])


def kafatasiSekmesi():
    root = tk.Tk()

    root.lift()
    root.wm_attributes("-topmost", True)
    root.wm_attributes("-disabled", True)
    root.wm_attributes("-transparentcolor", "black")
    # sekmedeki butonları kaldıran ve sekmeyi çerçevesiz yapan kod
    root.overrideredirect(True)
    # sekmenin boyutunu ayarlamayı kapatan kod
    root.resizable(False, False)

    ekran_genisligi = root.winfo_screenwidth()
    ekran_yuksekligi = root.winfo_screenheight()

    x_koordinati = (ekran_genisligi / 2) - (500 / 2)
    y_koordinati = (ekran_yuksekligi / 2) - (500 / 2)

    root.geometry("512x431+%d+%d" % (x_koordinati, y_koordinati))
    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load(DOOM_konum+'/download.gif')

    root.after(5000, lambda: root.destroy())

    root.mainloop()



def aciklamaSekmesi():


    pY = random.randint(0, 900)
    pX = random.randint(0, 1600)

    root2 = tk.Tk()

    root2.wm_attributes("-topmost",True)
    root2.wm_attributes("-disabled",True)
    root2.wm_attributes("-transparentcolor","black")
    root2.config(bg="black")

    # sekmedeki butonları kaldıran ve sekmeyi çerçevesiz yapan kod
    root2.overrideredirect(True)

    # sekmenin boyutunu ayarlamayı kapatan kod
    root2.resizable(False, False)

    root2.geometry("1920x1080")

    text = tk.Text(root2, bg="black", fg="red", bd=0, spacing1=5, font=('Stencil Std', 17, 'bold'))
    text.place(x=pX,y=pY)
    otomatikYazi(text, "1.0", "Tebrikler. Bilgisayarina virüs bulaştirdin\n"
                              "Bu virüsten kurtulmak için  \n bir testi geçmen gerekiyor\n"
                              "Bu test bir oyun olacak\n"
                              "Eger oyunu kazanabilirsen virüsten \n kurtulacaksin\n"
                              "Aksi takdirde oyunu geçene kadar \n virüs çalişmaya devam edecektir\n"
                              "Kolay gelsin\n"
                              "Bu ekran  kendini kapatacak \n ve oyun başlayacaktir")

    root2.after(25000, lambda: root2.destroy())

    root2.mainloop()


def sonSekme():


    pY = random.randint(0, 900)
    pX = random.randint(0, 1600)

    root2 = tk.Tk()

    root2.wm_attributes("-topmost",True)
    root2.wm_attributes("-disabled",True)
    root2.wm_attributes("-transparentcolor","black")
    root2.config(bg="black")

    # sekmedeki butonları kaldıran ve sekmeyi çerçevesiz yapan kod
    root2.overrideredirect(True)

    # sekmenin boyutunu ayarlamayı kapatan kod
    root2.resizable(False, False)

    root2.geometry("1920x1080")

    text = tk.Text(root2, bg="black", fg="red", bd=0, spacing1=5, font=('Stencil Std', 17, 'bold'))
    text.place(x=pX,y=pY)
    otomatikYazi(text, "1.0", "Tebrikler. Bilgisayarina virüs bulaştirdin\n"
                              "Bu virüsten kurtulmak için  \n bir testi geçmen gerekiyor\n"
                              "Bu test bir oyun olacak\n"
                              "Eger oyunu kazanabilirsen virüsten \n kurtulacaksin\n"
                              "Aksi takdirde oyunu geçene kadar \n virüs çalişmaya devam edecektir\n"
                              "Kolay gelsin\n"
                              "Bu ekran  kendini kapatacak \n ve oyun başlayacaktir")

    root2.after(25000, lambda: root2.destroy())
    root2.mainloop()
