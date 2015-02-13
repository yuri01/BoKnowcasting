__author__ = '0720046'

from tkinter import *
from dialogTable import demos # button callback handlers
from quitter import Quitter # attach a quit object to me


# class Demo(Frame):
#     def __init__(self, parent=None, **options):
#         Frame.__init__(self, parent, **options)
#         self.pack()
#         Label(self, text="Basic demos").pack()
#         for (key, value) in demos.items():
#             Button(self, text=key, command=value).pack(side=TOP, fill=BOTH)
#         Quitter(self).pack(side=TOP, fill=BOTH)

class Demo(Frame):
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        Label(self, text="분석 알고리즘").pack()
        for (k) in ['OLS','NN','SVM','GTB','ANN']:
            Checkbutton(self, text=k).pack(side=TOP, fill=BOTH)


if __name__ == '__main__': Demo().mainloop()