import imp
from db.repository import Repository
from models.partidos_model import PartidoModel

class PartidoRepository(Repository[PartidoModel]):
    def __init__(self):
        super().__init__()