from flask import jsonify, request, Blueprint
from controllers.results_controller import ResultController
# from decorators.logger_decorator import logger

results_module = Blueprint('resultados',__name__)
controller = ResultsController()

@results_module.get('/')
# @logger
def get_results():
  return jsonify(controller.get(request.args)
  
@results_module.post('/mesa/<string:table_id>/candidato/<string:candidate_id')
# @logger
def post_results(table_id, candidate_id):
  return jsonify(controller.post(request.get_json()),table_id, candidate_id), 201
  
@results_module.get('/<string:id>')
def results_by_table(id):
  return jsonify(controller.get_by_id(id))

@results_module.put('/<string:id>')
def update_table(id):
  controller.update(id, request.get_json())
  return jsonify({}), 204
  
@results_module.delete('/<string:id>')
def delete_table(id):
  controller.delete(id)
  return jsonify({}), 204