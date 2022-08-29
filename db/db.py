from distutils.command.config import config
import pymongo
from dotenv import dotenv_values

config = dotenv_values('.env')

class Db():
    def __init__(self) -> None:
        self.client = pymongo.MongoClient(config['DB_URL'])
        self.db = self.client.get_database()

    def collection(self, name):
        return self.db.get_collection(name)