from models.results_model import ResultsModel
from db.results_repository import ResultsRepository
from db.table_repository import TableRepository
from models.table_model import TableModel
from db.canditate_repository import CandidateRepository

class ResultsController():
    def __init__(self) -> None:
        self.repo = ResultsRepository()
        self.repo_table = TableRepository()
        # self.repo_candidate = CandidateRepository()

        #Retorna una lista
    def get(self, args):
        # print(args.to_dict())
        params = args.to_dict() # Recibe los argumentos en un diccionario 
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
    def post(self,data, table_id,candidate_id): 
        results = ResultsModel(data)
        table = self.repo_table.get_by_id(table_id)
        results.table = TableModel(table)
        candidate = self.repo_candidate.get_by_id(candidate_id)
        candidate[votes] = results.votes
        results.candidate = CandidateModel(candidate)

        #Validate some fields
        return {
        "id": self.repo.save(table)
        }
    #Método de actulizar 
    def update(self,id, data):
        results = ResultsModel(data)
        self.repo.update(id, results)
    
    #Método de eliminar
    def delete(self,id):
        self.repo.delete(id)



