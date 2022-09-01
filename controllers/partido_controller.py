from models.partidos_model import PartidoModel
from db.partido_repository import PartidoRepository

class PartidoController():
    
    def __init__(self) -> None:
     self.repo = PartidoRepository()
    
    #GET ALL = listar
    def get(self):
        return self.repo.get_all()
    #GET POR ID = buscar
    def get_by_id(self, id):
        return self.repo.get_by_id(id)
    
    def create(self, data):
        partido =PartidoModel(data)
        return {
            "id": self.repo.save(partido)
        }
    
    def update(self,id, data):
        partido =PartidoModel(data)
        self.repo.update(id, partido)
            
    def delete(self,id):
        self.repo.delete(id)
        