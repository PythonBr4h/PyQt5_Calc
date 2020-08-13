from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys, math
from Solution_of_equation.SOE import Other_UI


class UI(QtWidgets.QMainWindow):
	def __init__(self):
		super(UI, self).__init__()
		uic.loadUi('Calc_v4.ui', self)
		self.solution = []

	def btn_pressed_EC(self, k):
		global per_log
		try:
			# number Pi 'π'
			if k == 26:
				exec(f'self.lineEdit.setText(self.lineEdit.text() + "π")')
				self.solution.append(str(math.pi))
			# factorial
			if k == 29:
				exec(f'self.lineEdit.setText(self.lineEdit.text() + "!")')
				self.solution = [str(math.factorial(int("".join(self.solution))))]
			# working with sin()
			if k == 30:
				exec(f'self.lineEdit.setText(self.lineEdit.text() + "sin(")')
				self.solution.append("math.sin(")
			# working with cos()
			if k == 25:
				exec(f'self.lineEdit.setText(self.lineEdit.text() + "cos(")')
				self.solution.append("math.cos(")
			# working with e
			if k == 27:
				exec(f'self.lineEdit.setText(self.lineEdit.text() + "e")')
				self.solution.append("math.e")
			# working with log₁₀
			if k == 28:
				exec(f'self.lineEdit.setText(self.lineEdit.text() + "log")')
				per_log = 1
				self.solution.append('math.log(')
		except Exception as e:
			self.statusBar.showMessage(str(e))
			self.lineEdit.setText("")
			self.solution = [""]
		print(self.solution)

	def btn_pressed_DC(self, k):
		global per, start, per_log, p, pop
		try:
			# working with digits
			if k in a:
				if per_log == 1:
					exec(f'self.lineEdit.setText(self.lineEdit.text() + low_index[str(k)])')
					per_log = 2
					p = k
				elif per_log == 2:
					exec(f'self.lineEdit.setText(self.lineEdit.text() + self.pushButton_{k}.text())')
					pop += str(k)
				else:
					if set(self.lineEdit.text()) == {"0"}:
						exec(f'self.lineEdit.setText(self.pushButton_{k}.text())')
					else:
						exec(f'self.lineEdit.setText(self.lineEdit.text() + self.pushButton_{k}.text())')
					exec(f'self.solution.append(self.pushButton_{k}.text())')
					# this part for working with '√'
					if k == 13 and per == 1:
						print(per)
						start = 1
					elif start == 1 and k == 14:
						start = 0
						per = 0
						self.solution.append("**0.5")
					elif per == 1 and start == 0:
						per = 0
						self.solution.append("**0.5")
			# working with math actions
			elif k in b:
				if per_log == 2:
					exec(f"self.solution.append('{int(pop)}, {p})')")
					per_log, pop = 0, ""
				if self.lineEdit.text()[-1] not in "+-":
					exec(f'self.lineEdit.setText(self.lineEdit.text() + self.pushButton_{k}.text())')
				if k == 12:
					self.solution.append("*")
				elif k == 16:
					self.solution.append("/")
				else:
					exec(f'self.solution.append(self.pushButton_{k}.text())')
			# working with dot('.')
			elif k == 23:
				exec(f'self.lineEdit.setText(self.lineEdit.text() + ".")')
				self.solution.append(".")
			# clear lineEdit
			elif k == 17:
				self.solution = [""]
			# calculating
			elif k == 11:
				if per_log == 2:
					exec(f"self.solution.append('{int(pop)}, {p})')")
					per_log, pop = 0, ""
				if self.lineEdit.text() == "":
					pass
				else:
					self.lineEdit.setText(str(eval("".join(self.solution))))
					self.solution = [str(eval("".join(self.solution)))]
			# deleting last element
			elif k == 15:
				self.lineEdit.setText(self.lineEdit.text()[0:-1])
				self.solution = self.solution[0:-1]
			# working with '√'; require changes, please, checked "working with digits"
			elif k == 22:
				exec(f'self.lineEdit.setText(self.lineEdit.text() + "√")')
				per = 1
			# working with 'x²'
			elif k == 19:
				exec(f'self.lineEdit.setText(self.lineEdit.text() + "²")')
				self.solution.append("**2")
		except Exception as e:
			self.statusBar.showMessage(str(e))
			self.lineEdit.setText("")
			self.solution = [""]
		print(self.solution)

	def initUI(self):
		self.setFixedSize(352, 535)
		self.setWindowTitle("Calculator")
		self.setWindowOpacity(0.98)
		self.setWindowIcon(QIcon('calc_ico.png'))
		self.action.triggered.connect(self.EC)
		self.action_2.triggered.connect(self.DC)
		self.action_3.triggered.connect(self.SOE)
		self.show()

	def EC(self):
		self.setFixedSize(455, 535)
		self.lineEdit.setGeometry(QtCore.QRect(0, 0, 713, 61))

	def DC(self):
		self.setFixedSize(351, 535)
		self.lineEdit.setGeometry(QtCore.QRect(0, 0, 352, 61))

	def SOE(self):
		add_win.show()


if __name__ == "__main__":
	a = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 14)  # digits
	b = (10, 21, 12, 16, 20, 18)
	per, start, per_log, p, pop = 0, 0, 0, 0, ""
	low_index = {
		"0": "₀",
		"1": "₁",
		"2": "₂",
		"3": "₃",
		"4": "₄",
		"5": "₅",
		"6": "₆",
		"7": "₇",
		"8": "₈",
		"9": "₉",
	}

	app = QtWidgets.QApplication(sys.argv)
	root = UI()
	root.initUI()

	for i in range(0, 24):
		exec(f'root.pushButton_{i}.clicked.connect(lambda checked, text=i: root.btn_pressed_DC(text))')

	for i in range(25, 31):
		exec(f'root.pushButton_{i}.clicked.connect(lambda checked, text=i: root.btn_pressed_EC(text))')

	add_win = Other_UI()
	for i in range(20):
		exec(f'add_win.pushButton_{i}.clicked.connect(lambda checked, l=i:  add_win.pres(l))')

	app.exec_()
