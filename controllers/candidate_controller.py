from models.candidate_model import CandidateModel
from db.candidate_repository import CandidateRepository


class CandidateController():

    def __init__(self) -> None:
        self.repo = CandidateRepository()

# GET
    def get(self, args):
        params = args.to_dict()
        filter = {}

        if 'cedula' in params:
            if not '$and' in filter:
                filter['$and'] = []
            filter['$and'].append({
                'cedula': {
                    '$regex': f"^{params['cedula']}",
                    '$options': 'i'
                }
            })

        if 'numero_resolucion' in params:
            if not '$and' in filter:
                filter['$and'] = []
            filter['$and'].append({
                'numero_resolucion': {
                    '$gte': int(params['numero_resolucion'])
                }
            })
        if len(filter.keys()) == 0:
            return self.repo.get_all()
        return self.repo.query(filter)

    def getById(self, id):
        return self.repo.get_by_id(id)

# CREATE
    def create(self, data):
        candidate = CandidateModel(data)
        # Validate some fields
        return {
            "id": self.repo.save(candidate)
        }

# UPDATE
    def update(self, id, data):
        candidate = CandidateModel(data)
        self.repo.update(id, candidate)

# DELETE
    def delete(self, id):
        self.repo.delete(id)
