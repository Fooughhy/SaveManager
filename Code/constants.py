import os
from pathlib import Path
import tinydb

DB_REL_DIR = "database"
DB_FILE_NAME = "database.json"
# DB_REL_PATH = Path("database")
# DB_FILE_NAME = os.sep + "database.json"
# DB_ABS_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), DB_REL_PATH + DB_FILE_NAME)

DB_STORAGE_TYPE = tinydb.storages.JSONStorage
DB_TABLE_NAME = 'GameSaves'