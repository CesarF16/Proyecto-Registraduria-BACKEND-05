import json
from flask import jsonify, request, Blueprint
from controllers.candidate_controller import CandidateController
#from decorators.logger_decorator import logger

candidate_module = Blueprint('candidatos', __name__)
controller = CandidateController()


@candidate_module.get('/')
#@logger
def getCandidates():
    return jsonify(controller.get(request.args))


@candidate_module.post('/partidos/<string:partido_id>')
#@logger
def createCandidate(partido_id):
    # Devuelve 201 porque es un método POST
    return jsonify(controller.create(request.get_json(), partido_id)), 201


@candidate_module.get('/<string:id>')
def showCandidate(id):
    return jsonify(controller.get_by_id(id))


@candidate_module.put('/<string:id>')  # Esta ruta usará el método PUT:Editar
def updateCandidate(id):
    controller.update(id, request.get_json())
    return jsonify({}), 204


# DELETE:Borrar
@candidate_module.delete('/<string:id>')
def deleteCandidate(id):
    controller.delete(id)
    return jsonify({}), 204
