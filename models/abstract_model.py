from abc import ABCMeta

class AbstractModel(metaclass=ABCMeta):
    def __init__(self, data):
        for key, value in data.items():
            # revisar si la clase tiene los atributo y no crearlos
            setattr(self, key, value) #crea atributos que corresponden a las llaves del dic