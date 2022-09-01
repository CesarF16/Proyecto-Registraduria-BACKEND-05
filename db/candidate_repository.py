import imp
from db.repository import Repository
from models.candidate_model import CandidateModel

class CandidateRepository(Repository[CandidateModel]):
    def __init__(self):
        super().__init__()