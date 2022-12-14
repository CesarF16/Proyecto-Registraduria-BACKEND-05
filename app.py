from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import dotenv_values
#from db.db import Db
from routes.partidos_route import partido_module
from routes.table_routes import table_module
from routes.results_routes import results_module
from routes.candidates_route import candidate_module

config = dotenv_values('.env')
app = Flask(__name__)
cors = CORS(app)
#Db = Db() # instancia de la base de datos

app.register_blueprint(table_module, url_prefix="/mesa")
app.register_blueprint(partido_module, url_prefix="/partidos")
app.register_blueprint(results_module, url_prefix="/resultados")
app.register_blueprint(candidate_module, url_prefix="/candidatos")


@app.route('/')
def hello_world():
  dictToReturn = {'message': 'Hola mundo!'}
  return jsonify(dictToReturn)

if __name__ == '__main__':
  app.run(host='localhost', port=config["PORT"], debug=False)