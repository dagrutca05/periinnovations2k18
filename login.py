from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QGridLayout, QLabel, QLineEdit
import sys


class User(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		nameText = QLabel("Введите имя", self)
		nameText.move(50,50)

		self.nameInput = QLineEdit(self)
		self.nameInput.move(50, 70)
		surnameText = QLabel("Введите фамилия", self)
		surnameText.move(50,90)
		self.surnameInput = QLineEdit(self)
		self.surnameInput.move(50, 110)

		self.button = QPushButton("Войти", self)
		self.button.move(50, 135)
		self.button.clicked.connect(self.setForm)

		self.setGeometry(100, 100, 550, 550)
		self.setWindowTitle('Добро пожаловать')
		self.show()	

	def setForm(self):
		f = open("User list.txt")
		text = f.read()
		if self.nameInput.text() and surnameInput.text() in text:
			print("giuhtg")

app = QApplication(sys.argv)
my_window = User()
sys.exit(app.exec_())		
