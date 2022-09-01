from flask import jsonify, request, Blueprint
from controllers.table_controller import TableController
# from decorators.logger_decorator import logger

table_module = Blueprint('mesas',__name__)
controller = TableController()

@table_module.get('/')
# @logger
def get_table():
  return jsonify(controller.get(request.args))  

@table_module.post('/')
# @logger
def create_table():
  return jsonify(controller.create(request.get_json())), 201
  
@table_module.get('/<string:id>')
def show_table(id):
  return jsonify(controller.get_by_id(id))

@table_module.put('/<string:id>')
def update_table(id):
  controller.update(id, request.get_json())
  return jsonify({}), 204
  
@table_module.delete('/<string:id>')
def delete_table(id):
  controller.delete(id)
  return jsonify({}), 204