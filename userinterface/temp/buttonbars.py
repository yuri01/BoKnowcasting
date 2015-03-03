__author__ = '0720046'

from tkinter import *

class Checkbar(Frame):
    def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
        Frame.__init__(self, parent)
        self.vars = []
        for pick in picks:
            var = IntVar()
            chk = Checkbutton(self, text=pick, variable=var)
            chk.pack(side=side, anchor=anchor, expand=YES)
            self.vars.append(var)

    def state(self):
        return [var.get() for var in self.vars]

class Radiobar(Frame):
    def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
        Frame.__init__(self, parent)
        self.var = StringVar()
        self.var.set(picks[0])
        for pick in picks:
            rad = Radiobutton(self, text=pick, value=pick, variable=self.var)
            rad.pack(side=side, anchor=anchor, expand=YES)
    def state(self):
        return self.var.get()

if __name__ == '__main__':
    root = Tk()
    Freq = Checkbar(root, ['일', '주', '월'], side=TOP, anchor=NW)
    Label(root, text='주기', bg='white').pack()
    Agg = Radiobar(root, ['평균','중앙','최대','최소','최초','최후'], side=TOP, anchor=NW)
    Algo = Checkbar(root, ['OLS','NN','SVM','GTB','ANN'], side=TOP, anchor=NW)

    Freq.pack(side=LEFT, fill=Y)
    Agg.pack(side=LEFT, fill=Y)
    Algo.pack(side=LEFT)
    Freq.config(relief=RIDGE, bd=2)  # box line
    Agg.config(relief=RIDGE, bd=2)
    Algo.config(relief=RIDGE, bd=2)

    def allstates():
        print(Agg.state(), Freq.state(), Algo.state())

from userinterface.temp.quitter import Quitter
root.title('BOK Nowcasting')
Quitter(root).pack(side=RIGHT)
Button(root, text='Peek', command=allstates).pack(side=RIGHT)
root.mainloop()