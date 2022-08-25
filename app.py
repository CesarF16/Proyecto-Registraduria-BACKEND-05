from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import dotenv_values

config = dotenv_values('.env')
app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def hello_world():
  dictToReturn = {'message': 'Hola mundo!'}
  return jsonify(dictToReturn)

if __name__ == '__main__':
  app.run(host='localhost', port=config["PORT"], debug=False)