__author__ = '0720046'

from tkinter.filedialog import askopenfilename
from tkinter.colorchooser import askcolor
from tkinter.messagebox import askquestion, showerror
from tkinter.simpledialog import askfloat

# get standard dialogs
# they live in Lib\tkinter
demos = {
'Open': askopenfilename,
'Color': askcolor,
'Query': lambda: askquestion('Warning', 'You typed "rm *"\nConfirm?'), 'Error': lambda: showerror('Error!', "He's dead, Jim"),
'Input': lambda: askfloat('Entry', 'Enter credit card number')
}

mydemo={'FREQ' : ['일','주','월']}

AGG = ['평균','중앙','최대','최소','최초','최후']
Test = ['1회당 실험수','평균설명변수(확률)']
Algo = ['OLS','NN','SVM','GTB','ANN']
Genetic = ['버림:하위','남김:상위','신규추출','진화획수']
Sliding = ['기간','훈련횟수']