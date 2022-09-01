from typing import TypeVar, Generic, get_args # repositorio genérico
from db.db import Db
from bson import DBRef
from bson.objectid import ObjectId
from models.table_model import TableModel

T = TypeVar('T') # intancia del import repositorio genérico

class Repository (Generic[T]):

    def __init__(self):
        name = get_args(self.__orig_bases__[0] )[0].__name__.lower().replace('model','') # obtiene la clase y el nombre
        self.db = Db() # instancia de la base de datos
        self.collection = self.db.collection(name) # Devuelve las colecciones de la DB
    
    #get de la base de datos de las colecciones y serializarlo
    def get_all(self):
        results = self.collection.find() #respueta de la base de datos del object y tranformar a string
        data = []
        for r in results:
            r["_id"] = r["_id"].__str__() # accede al _id que lo trae como object id 
            r = self.transform_object_ids(r) # Métodos del repositorio para objetos compuestos
            r =  self.get_values_db_ref(r) #Métodos del repositorio 
            data.append(r) # agrega los valores a la lista 
        return data
    #filtrar información 
    def query(self, filter): 
        results = self.collection.find(filter)
        data = []
        for r in results:
            r["_id"] = r["_id"].__str__()
            r = self.transform_object_ids(r)
            r = self.get_values_db_ref(r)
            data.append(r)
        return data

    #agregaciones en MongoDB
    def query_aggregation(self, filter):
        data = []
        for x in self.collection.aggregate(filter):
            x["_id"] = x["_id"].__str__()
            x = self.transform_object_ids(x)
            x = self.get_values_db_ref(x)
            data.append(x)
        return data

    #Obtine la información a partir del Id
    def get_by_id(self, id):
        result = self.collection.find_one({"_id": ObjectId(id)})  
        result["_id"] = result["_id"].__str__()
        result = self.transform_object_ids(result)
        result = self.get_values_db_ref(result)
        return result

    #Método para guardar
    def save(self, item: T):
        item = self.transform_refs(item)
        id = ""
        #Si el objeto tiene ese Id y es diferente de vacio 
        #hasattr() toma como argumentos un objeto y el nombre de un atributo y retorna True si el objeto contiene dicho atributo.
        if hasattr(item, '_id') and item._id != "":
            #El item se tranforma en un Object Id 
            id = ObjectId(item._id)
            # Se actuliza la colección mediante el uso del Id, mediante sintaxis de MongoDB
            self.collection.update_one({
                "_id": id
            }, {
                "$set": item.__dict__
            })
        else:
            #Crear el objeto con el Id y se inserta 
            result = self.collection.insert_one(item.__dict__)
            id = result.inserted_id
        return id.__str__()
    
    #Método de actulizar 
    def update(self, id, item: T):
        #Recibe el id y lo transforma en object Id
        id = ObjectId(id)
        #actuliza el objeto en de un where
        self.collection.update_one({
            "_id": id
        }, {
            "$set": item.__dict__
        })
      
    #Método de eliminar
    def delete(self, id):
        #Recibe el id y lo transforma en object Id
        id = ObjectId(id)
        #Se envia el dato del id 
        self.collection.delete_one({
            "_id": id
        })

    #Utility methods to transform the responses
    def transform_object_ids(self, x):
        #Recibe la información del object id con sus llaves y las recorre 
        for attribute in x.keys():
            if isinstance(x[attribute], ObjectId): # si la llave es de tipo object Id
                x[attribute] = x[attribute].__str__() # conviente en una cadena de texto
            elif isinstance(x[attribute], list): # si la llave es de tipo lista
                x[attribute] = self.format_list(x[attribute]) # conviente en lista 
            elif isinstance(x[attribute], dict): # si la llave es de tipo diccionario 
                x[attribute]=self.transform_object_ids(x[attribute]) # transforma el objeto
        return x
    
    #Transformación en lista 
    def format_list(self, x):
        newList = []
        #Recibe la información del object id con sus llaves y las recorre 
        for item in x:
            # Si el objeto es un objectid lo agrega a la lista 
            if isinstance(item, ObjectId):
                newList.append(item.__str__())
            # si la lista es vacia se le asigna x
            if len(newList) == 0:
                newList = x
        return newList
    
    #Obtine los datos de la base de datos
    def get_values_db_ref(self, x):
        keys = x.keys()
        for k in keys:
            #DBRef --> referencia a la base de datos 
            if isinstance(x[k], DBRef):
                collection = self.db.collection(x[k].collection) # colección de la base de datos y la información de otras colecciones  
                valor = collection.find_one({"_id": ObjectId(x[k].id)}) # referencia por Id
                valor["_id"] = valor["_id"].__str__()
                x[k] = valor
                x[k] = self.get_values_db_ref(x[k])
            elif isinstance(x[k], list) and len(x[k]) > 0:
                x[k] = self.get_values_db_ref_from_list(x[k])
            elif isinstance(x[k], dict) :
                x[k] = self.get_values_db_ref(x[k])
        return x
    
    #Obtiene los datos y los transforma en lista
    def get_values_db_ref_from_list(self, theList):
        newList = []
        for item in theList:
            value = self.collection.find_one({"_id": ObjectId(item.id)})
            value["_id"] = value["_id"].__str__()
            newList.append(value)
        return newList
   
    #
    def transform_refs(self, item: T):
        theDict = item.__dict__
        keys = list(theDict.keys())
        for k in keys:
            if theDict[k].__str__().count("object") == 1:
                print(getattr(item, k))
                newObject = self.object_to_db_ref(getattr(item, k))
                setattr(item, k, newObject)
        return item

    #Crea la referencia con el objeto y el Id
    def object_to_db_ref(self, item: T):
        nameCollection = item.__class__.__name__.lower().replace('model','')
        return DBRef(nameCollection, ObjectId(item._id))


