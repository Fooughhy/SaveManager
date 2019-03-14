import json
import errno
from Code import constants
from pathlib import Path


class GameDatabase:

	def __init__(self):
		self.db_path = Path(constants.DB_REL_DIR, constants.DB_FILE_NAME)
		try:
			if self.db_path.absolute().is_file():
				with open(self.db_path, "r") as read_file:
					self.loaded_json_db = json.load(read_file)
			else:
				self.db_path.parent.mkdir(parents=True, exist_ok=True)
		except OSError as e:
			if e.errno != errno.EEXIST:
				raise


	def saveDatabaseAsJSON(self, json_database):
		try:
			with self.db_path.absolute().open("w") as write_file:
				json.dump(json_database, write_file)
		except OSError as e:
			if e.errno != errno.EEXIST:
				raise
