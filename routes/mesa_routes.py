from app import app
from flask import jsonify, Blueprint
from controllers.mesa_controlador import MesaControlador

mesa_modulo = Blueprint('mesa',__name__)
controller = MesaControlador()

#get
@mesa.get('/')
def get_all():
    mesa.get()
