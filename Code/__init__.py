import sys
from Code import GUI, Network
from PyQt5.QtWidgets import QApplication


def StartApp():
	my_app = QApplication(sys.argv)
	main_widget = GUI.QtWindow()

	database = Network.ParseDatabase()

	sys.exit(my_app.exec_())


StartApp()
