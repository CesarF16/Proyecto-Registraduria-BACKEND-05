from db.repository import Repository
from models.results_model import ResultsModel

class ResultsRepository(Repository[ResultsModel]):
    def __init__(self):
        super().__init__()