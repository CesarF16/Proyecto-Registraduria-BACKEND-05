from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import dotenv_values
#from db.db import Db

from routes.table_routes import table_module
from routes.candidates_route import candidate_module

config = dotenv_values('.env')
app = Flask(__name__)
cors = CORS(app)
#Db = Db() # instancia de la base de datos

app.register_blueprint(table_module, url_prefix="/mesa")
app.register_blueprint(candidate_module, url_prefix="/candidato")

@app.route('/')
def hello_world():
  dictToReturn = {'message': 'Hola mundo!'}
  return jsonify(dictToReturn)

if __name__ == '__main__':
  app.run(host='localhost', port=config["PORT"], debug=False)