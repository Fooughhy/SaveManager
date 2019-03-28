import sys
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import soupsieve
import collections
from collections import OrderedDict
from pprint import pprint
from tinydb.database import Document
import json


class Webpage:

	def __init__(self, page):
		super().__init__()

		self.game_database = {
			'name': 'Dark Souls',
			'save_location': '<Steam-folder>\\userdata\\<user-id>\\378540\\remote\\'
		}

		self.webpage = page
		self.webpage_content = self.request_webpage(page)

	def request_webpage(page):
		with urlopen(page) as url:
			mybytes = url.read()
			mystr = mybytes.decode("utf8")
			url.close()
		return mystr


# @staticmethod
def getDictFromHTMLTable(soup):
	if isinstance(soup, collections.Mapping) or isinstance(soup, list):
		table_dict = []
		for table in soup:
			values_dict = []
			for tr in table.select('tr'):
				for th, td in zip(tr.select('th'), tr.select('td')[::2]):
					temp_dict = {'Game': 'Life is Strange', 'System': th.text.strip(), 'Path': td.text.strip()}
					if not len(temp_dict):
						values_dict.append(temp_dict)
			if not len(values_dict):
				table_dict.append(values_dict)
		return table_dict
	else:
		values_dict = []
		for tr in soup.select('tr'):
			for th, td in zip(tr.select('th'), tr.select('td')[::2]):
				temp_dict = {'Game': 'Life is Strange', 'System': th.text.strip(), 'Path': td.text.strip()}
				if not len(temp_dict):
					values_dict.append(temp_dict)

	return values_dict
