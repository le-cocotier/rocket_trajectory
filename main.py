import math
import tkinter
import time


class Preview:
    def __init__(self):   
        self.masse = 600000
        self.g = 9.80665
        self.poids = self.masse * self.g
        self.alpha = math.radians(50)
        self.vitesse = 100
        self.t = 0
        self.x = 0
        self.y = 0

    def coo(self, color):
        print(self.alpha)
        self.x = self.vitesse * math.cos(self.alpha) * self.t
        self.y = -1/2 * self.g * self.t ** 2 + self.vitesse * math.sin(self.alpha) * self.t
        self.t += 0.05
        canvas.create_rectangle(self.x, self.y, self.x + 4, self.y + 4, fill=color)
        if self.y >= 0:
            fen.after(10, preview.coo)
        else:
            self.x = 0
            self.y = 0
            self.t = 0


    def increm_alpha(self, value):
        self.alpha += math.radians(value)
        self.coo('blue')


fen = tkinter.Tk()
canvas = tkinter.Canvas(fen, width=1000, height=700, bg='black')
canvas.pack()
preview = Preview()
preview.coo('white')
print('salut')

fen.bind('<z>', lambda x: preview.increm_alpha(1))
fen.bind('<s>', lambda x: preview.increm_alpha(-1))


fen.mainloop()