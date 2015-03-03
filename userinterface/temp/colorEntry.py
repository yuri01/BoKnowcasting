__author__ = '0720046'

from tkinter import *



class Demo(Frame):
    colors = ['버림: 하위(%)','남김: 상위(%)','신규 추출(%)','진화 횟수(회)']
    r = 0
    for c in colors:
        Label(text=c, relief=RIDGE, width=20).grid(row=r, column=0)
        Entry(bg='green', relief=SUNKEN, width=20).grid(row=r, column=1)
        r += 1
    # Frame.title('진화프로세스')
    # Label(Frame, text='1회 실험후 결과값 처리기준', bg='white').pack()



if __name__ == '__main__': Demo().mainloop()