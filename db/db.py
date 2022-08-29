from mimetypes import init

import pymongo # importación de Mongo
from dotenv import dotenv_values

config = dotenv_values('.env') #llamado de las variables de entorno

#Clase que contiene la conexión de la base de datos
class Db:
  def __init__(self): 
    self.client = pymongo.MongoClient(config['DB_URL']) # conexión col el cliente DB
    self.db = self.client.get_database() # Referencia a la base de datos trae la información
    
  def collection(self, name):
    return self.db.get_collection(name)