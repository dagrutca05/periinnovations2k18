import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QGridLayout, QLabel, QLineEdit, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


class Project(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):

#ОКНО 1
		self.count = 0 # переменная содержащая количество правильных ответов

		self.window1 = QWidget()
		grid1 = QGridLayout()
		grid1.setSpacing(10)

		self.photo1 = QPushButton('Кадр из фильма')
		self.photo1.setIcon(QIcon("pok.jpg"))
		self.photo1.setIconSize(QSize(350,200))


		self.button1 = QPushButton('Неправильный ответ')
		self.button2 = QPushButton('Неправильный ответ')
		self.button3 = QPushButton('Неправильный ответ')
		self.button4 = QPushButton('Правильный ответ')


		self.button1.clicked.connect(self.perehod)
		self.button2.clicked.connect(self.perehod)
		self.button3.clicked.connect(self.perehod)
		self.button4.clicked.connect(self.perehod)

		grid1.addWidget(self.photo1, 0, 0)
		grid1.addWidget(self.button1, 1, 0)
		grid1.addWidget(self.button2, 1, 1)
		grid1.addWidget(self.button3, 2, 0)
		grid1.addWidget(self.button4, 2, 1)


		self.window1.setLayout(grid1)
		self.setCentralWidget(self.window1)

		self.button1.clicked.connect(self.inright1)
		self.unright = QLabel('                                                 ')
		grid1.addWidget(self.unright, 3,1)
			
		self.button2.clicked.connect(self.inright1)
		self.unright = QLabel('                                                 ')
		grid1.addWidget(self.unright, 3,1)

		self.button3.clicked.connect(self.inright1)
		self.unright = QLabel('                                                 ')

		self.scores = QLabel('0')
		grid1.addWidget(self.scores, 3, 0)
		grid1.addWidget(self.unright, 3,1)




#ОКНО 2


		self.window2 = QWidget()
		grid2 = QGridLayout()
		grid2.setSpacing(10)


		self.photo2 = QPushButton('Кадр из фильма')
		self.photo2.setIcon(QIcon("pok.jpg"))
		self.photo2.setIconSize(QSize(350,200))


		self.button5 = QPushButton('Правильный ответ')
		self.button6 = QPushButton('Неправильный ответ')
		self.button7 = QPushButton('Неправильный ответ')
		self.button8 = QPushButton('Неправильный ответ')

		self.button5.clicked.connect(self.perehod)
		self.button6.clicked.connect(self.perehod)
		self.button7.clicked.connect(self.perehod)
		self.button8.clicked.connect(self.perehod)

		grid2.addWidget(self.photo2, 0, 0)
		grid2.addWidget(self.button5, 1, 0)
		grid2.addWidget(self.button6, 1, 1)
		grid2.addWidget(self.button7, 2, 0)
		grid2.addWidget(self.button8, 2, 1)


		self.window2.setLayout(grid2)

		self.setGeometry(100, 100, 850, 850)
		self.setWindowTitle('Угадай фильм')
		self.show()

		grid2.addWidget(self.scores, 3, 0)

#OKNO 3

		self.window3 = QWidget()
		grid3 = QGridLayout()
		grid3.setSpacing(10)


	def perehod(self):
		context = self.sender()
		if context.text() == 'Правильный ответ':
			self.count += 1

		self.scores.setText(str(self.count))
		self.setCentralWidget(self.window2)

	def startGame(self):
		self.scores.setText("0")
		self.startButton.setEnabled(False)

	def inright1(self):
		self.unright.setText('Неправильно')

	def inright2(self):
		self.unright2.setText('Неправильно')

	def doAction(self):
		sender = self.sender()
		temp_scores = int(self.scores.text()) + 1
		self.scores.setText(str(temp_scores))

app = QApplication(sys.argv)
my_window = Project()
sys.exit(app.exec_())
