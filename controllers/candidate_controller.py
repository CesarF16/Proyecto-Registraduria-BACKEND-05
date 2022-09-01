from db.candidate_repository import CandidateRepository
from db.partido_repository import PartidoRepository
from models.candidate_model import CandidateModel
from models.partidos_model import PartidoModel


class CandidateController():

    def __init__(self) -> None:
        self.repo = CandidateRepository()
        self.repo_partido = PartidoRepository()
        
    def get(self, args):
        return self.repo.get_all()


    def get_by_id(self, id):
        return self.repo.get_by_id(id)


    def create(self, data, partido_id):
        candidate = CandidateModel(data)
        partido = self.repo_partido.get_by_id(partido_id)
        candidate.partido = PartidoModel(partido)
        return {
            "id": self.repo.save(candidate)
        }


    def update(self, id, data):
        candidate = CandidateModel(data)
        self.repo.update(id, candidate)


    def delete(self, id):
        self.repo.delete(id)