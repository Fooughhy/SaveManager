import sys
from Code import GUI, Network, Database, constants
from PyQt5.QtWidgets import QApplication
from pathlib import Path


def StartApp():
	my_app = QApplication(sys.argv)
	main_widget = GUI.QtWindow()

	test_db = """
{
	"researcher": {
		"name": "Ford Prefect",
		"species": "Betelgeusian",
		"relatives": [
			{
				"name": "Zaphod Beeblebrox",
				"species": "Betelgeusian"
			}
		]
	}
}
"""

	database = Database.GameDatabase()
	networkdb = Network.ParseDatabase()

	database.saveDatabaseAsJSON(test_db)

	sys.exit(my_app.exec_())


StartApp()
