from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
import sys, math
from decimal import Decimal


class Other_UI(QtWidgets.QMainWindow):
	def __init__(self):
		super(Other_UI, self).__init__()
		self.equation = ""
		uic.loadUi('C:\Programming\Python Programming\PyQtDesigner\Calculator\V4\Solution_of_equation\Solution_of_equation_v1.ui', self)
		self.initUI()
		self.ka, self.kb, self.kc = 0, 0, 0

	def initUI(self):
		self.setFixedSize(352, 441)
		self.setWindowTitle("Solution of equation")
		self.setWindowIcon(QIcon('../V4/calc_ico.png'))

	def pres(self, k):
		try:
			if self.lineEdit.text() == "" and k not in [11, 13, 15]:
				exec(f'self.lineEdit.setText(self.lineEdit.text() + self.pushButton_{k}.text())')
			elif k in (10, 12, 14, 17):
				if k == 12:
					exec(f'self.lineEdit.setText(self.lineEdit.text() + "*")')
				elif k == 14:
					exec(f'self.lineEdit.setText(self.lineEdit.text() + "/")')
				else:
					exec(f'self.lineEdit.setText(self.lineEdit.text() + " " + self.pushButton_{k}.text() + " ")')
			elif k in range(0, 10) or k in [18, 19]:
				exec(f'self.lineEdit.setText(self.lineEdit.text() + self.pushButton_{k}.text())')
			elif k == 15:
				self.lineEdit.setText("")
				self.equation = ""
			elif k == 11:
				self.get_equation()
			elif k == 16:
				exec(f'self.lineEdit.setText(self.lineEdit.text() + "²")')
			elif k == 13:
				self.lineEdit.setText(self.lineEdit.text()[0:-1])
		except Exception as e:
			self.statusBar.showMessage(str(e))
			self.lineEdit.setText("")
			self.equation = ""

	def get_equation(self):
		self.equation = self.lineEdit.text().split()
		print(self.equation)
		self.solution()

	def solution(self):
		# finding a, b, c
		for i in range(len(self.equation)):
			if "x²" in self.equation[i]:
				self.ka = 1
				if "".join(self.equation[i].split("x²")) == "":
					self.a = 1
				elif "".join(self.equation[i].split("x²")) == "-":
					self.a = -1
				elif i == 0:
					self.a = float(eval("".join(self.equation[i].split("x²"))))
				elif i != 0:
					self.a = float(eval(self.equation[i - 1] + "".join(self.equation[i].split("x²"))))
				print(str(self.a) + " - a")
			elif "x" in self.equation[i]:
				self.kb = 1
				if "".join(self.equation[i].split("x")) == "":
					self.b = 1
				elif "".join(self.equation[i].split("x")) == "-":
					self.b = -1
				elif i == 0:
					self.b = float(eval("".join(self.equation[i].split("x"))))
				elif i != 0:
					self.b = float(eval(self.equation[i - 1] + "".join(self.equation[i].split("x"))))
				print(str(self.b) + " - b")
			elif "x" not in self.equation[i] and "+" != self.equation[i] and "-" != self.equation[i]:
				self.kc = 1
				if i == 0:
					self.c = float(eval(self.equation[i]))
				elif i != 0:
					self.c = float(eval(self.equation[i - 1] + self.equation[i]))
				print(str(self.c) + " - c")
		if self.kc == 0:
			self.c = 0
		if self.kb == 0:
			self.b = 0
		if self.ka == 0:
			QMessageBox.about(self, "Roots", f'x = {-self.c / self.b}')
		# finding roots
		D = self.b ** 2 - 4 * self.a * self.c
		if D < 0:
			QMessageBox.about(self, "Roots", "No roots")
		if D == 0:
			x = -self.b / (2 * self.a)
			if Decimal(x).as_integer_ratio()[0] > 10000 or Decimal(x).as_integer_ratio()[1] > 10000:
				pass
			elif x != int(x):
				x = str(Decimal(x).as_integer_ratio()[0]) + "/" + str(Decimal(x).as_integer_ratio()[1])
			else:
				x = int(x)
			QMessageBox.about(self, "Roots", f'Roots: x = {x}')
		else:
			x1 = (-self.b + D ** 0.5) / (2 * self.a)
			x2 = (-self.b - D ** 0.5) / (2 * self.a)
			# Converting float to in
			if self.a == int(self.a):
				self.a = int(self.a)
			if self.b == int(self.b):
				self.b = int(self.b)
			if D == int(D):
				D = int(D)
			if D ** 0.5 != int(D ** 0.5):
				x1 = str(-self.b) + "+" + "√" + str(D) + "/" + str(2 * self.a)
			elif Decimal(x1).as_integer_ratio()[0] > 10000 and Decimal(x1).as_integer_ratio()[1] > 10000:
				x1 = (-self.b + D ** 0.5) / (2 * self.a)
			elif x1 != int(x1):
				x1 = str(Decimal(x1).as_integer_ratio()[0]) + "/" + str(Decimal(x1).as_integer_ratio()[1])
			else:
				x1 = int(x1)

			if D ** 0.5 != int(D ** 0.5):
				x2 = str(-self.b) + "-" + "√" + str(D) + "/" + str(2 * self.a)
			elif Decimal(x2).as_integer_ratio()[0] > 10000 and Decimal(x2).as_integer_ratio()[1] > 10000:
				x2 = (-self.b - D ** 0.5) / (2 * self.a)
			elif x2 != int(x2):
				x2 = str(Decimal(x2).as_integer_ratio()[0]) + "/" + str(Decimal(x2).as_integer_ratio()[1])
			else:
				x2 = int(x2)
			QMessageBox.about(self, "Roots", f'x₁ = {x1}\n'
											 f'x₂ = {x2}')


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	win = Other_UI()
	win.show()

	for i in range(20):
		exec(f'win.pushButton_{i}.clicked.connect(lambda checked, l=i:  win.pres(l))')

	app.exec_()
