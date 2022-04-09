from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class MyLayout(GridLayout):
	def se_value(self, event):
		if  not event.text:
			self.steps += 1
			event.text = self.player
			# self.player = int(not self.player)
			if self.player == "O":
				self.player = "X"
			else:
				self.player = "O"

		for all_rows in self.board:
			print (all_rows[0])
			for item in list(all_rows[0]):
				# print (item)
				if item.text == "O":
					self.row +=1
				elif item.text == "X":
					self.col +=1
			for item in list(all_rows[1]):
				if item.text == "O":
					self.row +=1
				elif item.text == "X":
					self.col +=1
			for item in list(all_rows[2]):
				if item.text == "O":
					self.row +=1
				elif item.text == "X":
					self.col +=1

		print (self.row)
		print (self.col)
		if self.steps == 9:
			print("draw")
			# print (Label(text = "Draw"))

	def make_board(self):
		self.board =[]
		for row in range(3):
			line = []
			for col in range(3):
				button =  Button(text='')
				button.bind(on_press = self.se_value)
				line.append(button)
			self.board.append(line)

	def __init__(self):
		super(MyLayout, self).__init__()
		self.steps = 0
		self.row = 0
		self.col = 0
		self.player = "O"
		self.cols = 3
		self.rows = 3
		# self.add_widget(Button(text=""))
		self.make_board()
		for row in self.board:
			for item in row:
				self.add_widget(item)
class MyApp(App):
	def build(self):
		# return Label(text="hellow world")
		return MyLayout()
MyApp().run()