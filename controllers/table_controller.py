from models.table_model import TableModel
from db.table_repository import TableRepository

class TableController():

    def __init__(self) -> None:
        self.repo = TableRepository()
    
    #Retorna una lista 
    def get(self, args):
        # print(args.to_dict())
        params = args.to_dict() # Recibe los argumentos en un diccioanrio 
        filter = {}
        #Realizar los filtros con el query
        if 'numero' in params:
            if not '$and' in filter:
                filter['$and'] = []
            filter['$and'].append({
                'numero': {
                '$regex': f"^{params['numero']}",
                '$options': 'i'
                }
            })
        
        if 'cantidad_inscritos' in params:
            if not '$and' in filter:
                filter['$and'] = []
            filter['$and'].append({
                'cantidad_inscritos': {
                '$gte': int(params['cantidad_inscritos'])
                }
            })
        if len(filter.keys()) == 0:
            return self.repo.get_all()
        return self.repo.query(filter)

    def get_by_id(self,id):
        return self.repo.get_by_id(id)
  
    #Método de creación de la mesa
    def create(self,data):
        table = TableModel(data)
        #Validate some fields
        return {
        "id": self.repo.save(table)
        }
    #Método de actulizar 
    def update(self,id, data):
        table = TableModel(data)
        self.repo.update(id, table)
    
    #Método de eliminar
    def delete(self,id):
        self.repo.delete(id)



