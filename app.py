from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import dotenv_values
from routes.mesa_routes import mesa_modulo

config = dotenv_values('.env')
app = Flask(__name__)
cors = CORS(app)

app.register_blueprint(mesa_modulo, url_prefix ='/mesas')

@app.route('/')
def hello_world():
  dictToReturn = {'message': 'Hola mundo!'}
  return jsonify(dictToReturn)

if __name__ == '__main__':
  app.run(host='localhost', port=config["PORT"], debug=False)