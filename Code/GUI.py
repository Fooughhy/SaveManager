# GUI Frameworks: PyQt, Pyforms, Kivy

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QHBoxLayout


class QtWindow(QWidget):

	def __init__(self):
		super().__init__()

		self.game_database = {
				'name': 'Dark Souls',
				'save_location': '<Steam-folder>\\userdata\\<user-id>\\378540\\remote\\'
		}

		self.init_ui()

	def init_ui(self):
		window_rectangle = QtCore.QRect(100, 100, 700, 400)

		self.setWindowTitle('GameSave Manager')
		self.setWindowIconText('Hello')
		self.setGeometry(window_rectangle)

		h_box = QHBoxLayout()
		v_box = QVBoxLayout()

		test_label = QLabel(self)
		test_label.setText('Test text')
		test_label.move(100, 100)
		h_box.addStretch()
		h_box.addWidget(test_label)
		h_box.addStretch()

		v_box.addStretch()
		v_box.addLayout(h_box)
		v_box.addStretch()

		self.setLayout(v_box)

		self.show()
