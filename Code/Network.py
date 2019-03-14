import sys
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import soupsieve
from collections import OrderedDict
from pprint import pprint


class ParseDatabase:

	def __init__(self, *args, **kwargs):
		super().__init__()

		self.game_database = {
			'name': 'Dark Souls',
			'save_location': '<Steam-folder>\\userdata\\<user-id>\\378540\\remote\\'
		}

		self.request_webpage()

	def request_webpage(self):
		with urlopen("https://pcgamingwiki.com/wiki/The_Surge") as url:
			mybytes = url.read()
			mystr = mybytes.decode("utf8")
			url.close()

		soup = BeautifulSoup(mystr, features='html.parser')
		# soup = BeautifulSoup(mystr, features='html5lib')

		# selector = 'h3 ~ div > #Save_game_data_location'
		# template - infotable - head
		# table - gamedata - head - row
		# first_selector = 'span#Save_game_data_location  table#table-gamedata'
		# second_selector = 'span#Save_game_data_location'

		# found = soup.select(first_selector)
		# print(found)

		table_html = soup.find('span', {'id': 'Save_game_data_location'}).find_next('table', {'id': 'table-gamedata'})
		print(table_html)
		# selector = 'span#Save_game_data_location  table#table-gamedata'
		selector = 'h3 ~ div.container-pcgwikitable table#table-gamedata.pcgwikitable.template-infotable'
		table_html = soupsieve.select_one(selector, soup)
		print(table_html)
		# found2 = found.find_next('table', {'id': 'table-gamedata'})

		# print(table_html.text)
		# print(table_html)
		d = self.getDictFromHTMLTable(table_html)
		dd = [soupsieve.closest('span#Save_game_data_location', soup), d]

		#Save_game_data_location

		pprint(d)
		pprint(dd)

		# print(found2)
		# print(found2)
		# print(type(found2))

	def getDictFromHTMLTable(self, table_html):
		values_dict = OrderedDict()
		try:
			for tr in table_html.select('tr'):
				for th, td in zip(tr.select('th'), tr.select('td')[::2]):
					values_dict[th.text.strip()] = td.text.strip().splitlines()
		except TypeError:
			print("Provided table is of type: " + type(table_html))

		# table_dict = [values_dict]
		# for tr in table_html.select('tr'):
		# 	for th, td in zip(tr.select('th'), tr.select('td')[::2]):
		# 		values_dict[th.text.strip()] = td.text.strip().splitlines()

		return values_dict
