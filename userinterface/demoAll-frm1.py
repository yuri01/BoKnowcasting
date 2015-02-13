__author__ = '0720046'

from tkinter import *
from quitter import Quitter

demoModules = ['demoDlg', 'demoDlg1', 'demoDlg2', 'demoScale', 'demoScale1']
parts = []

def addComponents(root):
    for demo in demoModules:
        module = __import__(demo) # import by name string
        part = module.Demo(root) # attach an instance
        part.config(bd=2, relief=GROOVE) # or pass configs to Demo()
        part.pack(side=LEFT, expand=YES, fill=BOTH) # grow, stretch with window
        parts.append(part) # change list in-place

def dumpState():
    for part in parts: # run demo report if any
        print(part.__module__ + ':', end=' ')
        if hasattr(part, 'report'):
            part.report()
        else:
            print('none')

root = Tk() # make explicit root first
root.title('BOK GDP Nowcasting')
Label(root, text='Input 조건 설정', bg='white').pack()
addComponents(root)
Button(root, text='조건입력', command=dumpState).pack(fill=X)
Quitter(root).pack(fill=X)
root.mainloop()