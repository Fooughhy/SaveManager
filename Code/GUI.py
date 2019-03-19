# GUI Frameworks: PyQt, Pyforms, Kivy

from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QMainWindow


class QtWindow(QWidget):

	def __init__(self, db):
		super(QWidget, self).__init__()

		self.game_database = db

		self.init_ui()

	def init_ui(self):
		window_rectangle = QtCore.QRect(100, 100, 700, 400)

		self.setWindowTitle('GameSave Manager')
		self.setWindowIconText('Hello')
		self.setGeometry(window_rectangle)

		h_box = QHBoxLayout()
		v_box = QVBoxLayout()

		backup_button = QPushButton('Backup saves')
		backup_button.move(200, 200)
		backup_button.clicked.connect(self.backupGames)

		test_label = QLabel('Test text')
		test_label.move(100, 100)
		h_box.addStretch()
		h_box.addWidget(test_label)
		h_box.addWidget(backup_button)
		h_box.addStretch()

		v_box.addStretch()
		v_box.addLayout(h_box)
		v_box.addStretch()

		self.setLayout(v_box)

	@pyqtSlot()
	def backupGames(self):
		item = self.game_database.getGamePath('Life is Strange')
		print(item)
