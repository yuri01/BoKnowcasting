# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 12:26:52 2015

@author: yuri
"""

"create a bar of check buttons that run dialog demos"


import os
os.getcwd()
os.chdir("/Users/yuri/Documents/python/Nowcasting")


from tkinter import *
from dialogTable import demos 
from quitter import Quitter
# get base widget set
# get canned dialogs
# attach a quitter object to "me"

FREQ = ['일','주','월']
AGG = ['평균','중앙','최대','최소','최초','최후']
Test = ['1회당 실험수','평균설명변수(확률)']
Algo = ['OLS','NN','SVM','GTB','ANN']
Genetic = ['버림:하위','남김:상위','신규추출','진화획수']
Sliding = ['기간','훈련횟수']

class Demo(Frame):
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options) 
        self.pack()
        self.tools()
        Label(self, text="Check demos").pack() 
        self.vars = []
        for k in FREQ: 
            var = IntVar()
#            Checkbutton(self, text=k,variable=var,command=demos[key]).pack(side=LEFT) 
            Checkbutton(self, text=k,variable=var).pack(side=LEFT)             
            self.vars.append(var)

        for i in AGG:
            Checkbutton(self, text=i).pack(side=LEFT) 
            
        for j in Algo:
            Checkbutton(self, text=j).pack(side=RIGHT) 
            
    def report(self):
        for var in self.vars:
            print(var.get(), end=' ') 
        print()
    
    def tools(self):
        frm = Frame(self) 
        frm.pack(side=RIGHT)
        Button(frm, text='State', command=self.report).pack(fill=X) 
        Quitter(frm).pack(fill=X)

if __name__ == '__main__': Demo().mainloop()