__author__ = '0720046'

from tkinter import *
from userinterface.temp.dialogTable import demos # button callback handlers
from userinterface.temp.quitter import Quitter # attach a quit object to me


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
        Label(self, text="데이터주기").pack()
        for (k) in ['일','주','월']:
            Checkbutton(self, text=k).pack(side=TOP, fill=BOTH)


if __name__ == '__main__': Demo().mainloop()