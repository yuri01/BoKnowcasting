__author__ = '0720046'

"create two linked scales used to launch dialog demos"
from tkinter import * # get base widget set
from dialogTable import demos # button callback handlers
from quitter import Quitter # attach a quit frame to me

class Demo(Frame):
	def __init__(self, parent=None, **options):
		Frame.__init__(self, parent, **options)
		self.pack()
		Label(self, text="Training").pack()
		self.var = IntVar()
		Scale(self, label='1회당 실험수',
					command=self.onMove, # catch moves
					variable=self.var, # reflects position
					from_=0, to=100, showvalue=YES, orient='horizontal',length=200).pack()
		Scale(self, label='평균설명변수(확률)',
					command=self.onMove, # catch moves
					variable=self.var, # reflects position
					from_=0, to=100, showvalue=YES, orient='horizontal',length=200).pack()

		# Scale(self, label='훈련기간',
		# 			command=self.onMove, # catch moves
		# 			variable=self.var, # reflects position
		# 			from_=0, to=len(demos)-1,
		# 			length=200, tickinterval=1,
		# 			showvalue=YES, orient='horizontal').pack()
		# Quitter(self).pack(side=RIGHT)
		# Button(self, text="Run demo", command=self.onRun).pack(side=LEFT)
		# Button(self, text="State", command=self.report).pack(side=RIGHT)

	def onMove(self, value):
		print('in onMove', value)

	def onRun(self):
		pos = self.var.get()
		print('You picked', pos)
		demo = list(demos.values())[pos] # map from position to value (3.X view)
		print(demo()) # or demos[ list(demos.keys())[pos] ]()

	def report(self):
		print(self.var.get())

if __name__ == '__main__':
	print(list(demos.keys()))
	Demo().mainloop()
