import sys
from Code import GUI, Network, Database, constants
from PyQt5.QtWidgets import QApplication
from pathlib import Path
from bs4 import BeautifulSoup
import soupsieve
import collections
from tinydb import TinyDB, Query
from tinydb.database import Table
from tinydb.queries import Query


def StartApp():
	my_app = QApplication(sys.argv)
	database = Database.GameDatabase()
	network_html = Network.request_webpage()
	main_widget = GUI.QtWindow(database)

	main_widget.show()

	soup = BeautifulSoup(network_html, features='html.parser')

	# Alternate parser for HTML
	# soup = BeautifulSoup(mystr, features='html5lib')

	# selector: Used to select tables containing data on the webpage
	selector = 'h3 ~ div.container-pcgwikitable table#table-gamedata.pcgwikitable.template-infotable'
	table_html = soupsieve.select(selector, soup)
	if isinstance(table_html, collections.Mapping) or isinstance(table_html, list):
		for t in table_html:
			d = Network.getDictFromHTMLTable(t)
			for doc in d:
				database.db.insert(doc)

	sys.exit(my_app.exec_())


StartApp()
