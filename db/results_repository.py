from db.repository import Repository
from models.results_model import ResultsModel
from bson import ObjectId

class ResultsRepository(Repository[ResultsModel]):
    def __init__(self):
        super().__init__()

    #Total de resultados
    def get_resultado_total(self):
        data = self.get_all()
        result = {"results": {}}
        for register in data:
            if register["candidate"]["nombre"] + " " + register["candidate"]["apellido"] not in result["results"]:
                result["results"].update({register["candidate"]["nombre"] + " " + register["candidate"]["apellido"]:1})
            else:
                result["results"][register["candidate"]["nombre"] + " " + register["candidate"]["apellido"]] +=  1
        return result
    
    #Total resultado por cadidato
    def total_candidato(self, candidato_id):
        filter = {"candidate.$id": ObjectId(candidato_id)}
        data = self.query(filter)
        result = {}
        for register in data:      
            if register["candidate"]["nombre"] + " " + register["candidate"]["apellido"] not in result:
                result.update({register["candidate"]["nombre"] + " " + register["candidate"]["apellido"]:1})
            else:
                result[register["candidate"]["nombre"] + " " + register["candidate"]["apellido"]] +=  1
        return result

    def aux(self, dict_aux, register):
        if register["candidate"]["nombre"] + " " + register["candidate"]["apellido"] not in dict_aux:
            dict_aux[register["candidate"]["nombre"] + " " + register["candidate"]["apellido"]]=1
        else:
            dict_aux[register["candidate"]["nombre"] + " " + register["candidate"]["apellido"]] +=1
        return dict_aux

    #Total resultados por mesas
    def get_total_mesa(self): 
        data = self.get_all()
        result = {}
        for register in data:
            if register["table"]["numero"] not in result:
                result[register["table"]["numero"]] = {register["candidate"]["nombre"] + " " + register["candidate"]["apellido"]:1}
            else:
                dict_aux = result[register["table"]["numero"]]
                result[register["table"]["numero"]] = self.aux(dict_aux,register)
        return result    

    #Total resultados por partido
    def get_total_partido(self):
        data = self.get_all()
        result = {}
        for register in data:
            nom_partido = register["candidate"]["partido"]["nombre"]
            if nom_partido not in result:
                result[nom_partido] = {register["candidate"]["nombre"] + " " + register["candidate"]["apellido"]:1}
            else:
                dict_aux = result[nom_partido]
                result[nom_partido] = self.aux(dict_aux,register)
        return result


