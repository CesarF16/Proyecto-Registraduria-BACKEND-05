import imp
from db.repository import Repository
from models.table_model import TableModel

class TableRepository(Repository[TableModel]):
    def __init__(self):
        super().__init__()