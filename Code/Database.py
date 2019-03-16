import json
import errno
from Code import constants
from pathlib import Path
from tinydb import Query
from tinydb.database import TinyDB, Table


class GameDatabase:

	def __init__(self, storage_type=constants.DB_STORAGE_TYPE
				, abs_path=Path(constants.DB_REL_DIR, constants.DB_FILE_NAME).absolute()):

		self.db = TinyDB(abs_path, storage=storage_type)
		self.db_path = Path(abs_path)
		#
		# try:
		# 	if self.db_path.absolute().is_file():
		# 		with open(self.db_path, "r") as read_file:
		# 			self.loaded_json_db = json.load(read_file)
		# 	else:
		# 		self.db_path.parent.mkdir(parents=True, exist_ok=True)
		# except OSError as e:
		# 	if e.errno != errno.EEXIST:
		# 		raise

	# def saveDatabaseAsJSON(self, json_database):
	# 	self.db.table()
	# 	try:
	# 		with self.db_path.absolute().open("w") as write_file:
	# 			# json.dump(json_database, write_file)
	# 			return
	# 	except OSError as e:
	# 		if e.errno != errno.EEXIST:
	# 			raise

	def getGamePath(self, game_name):
		return self.db.search(Query()['game'] == 'Life is Strange')
