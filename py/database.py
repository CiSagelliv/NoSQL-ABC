from pymongo import MongoClient

def getDB():
    host = "localhost"
    puerto = "27017"
    usuario = "parzibyte"
    palabra_secreta = "hunter2"
    base_de_datos = "suicides"
    cliente = MongoClient("mongodb://{}:{}".format(host, puerto))
    return cliente[base_de_datos]

def insert(**kwargs):
    db = getDB()
    resultado = db.rates.insert_one(kwargs)

def update(country_year, **actCampos):
    """
        Recibe como argumentos el id de la base de datos y actCampos,
        dentro del método actualiza los campos del diccionario 
        sin contar el id de los datos
    """
    db = getDB()
    resultado = db.rates.update_one({
           "country_year":country_year          
        }, {
           '$set': actCampos
        })
    return resultado.modified_count

def buscaUpdate(country_year):
    db = getDB()
    result = db.rates.find_one({"country_year":country_year})
    return result

# Método de eliminar
def delete(country,sex,age,generation):
    db = getDB()
    deleteFilter = {
        "country": country,
        "sex": sex,
        "age": age,
        "generation": generation,
    }
    resultado = db.rates.delete_one(deleteFilter)
    return resultado.deleted_count;

def findAll():
    db = getDB()
    return db.rates.find({},{
        "_id":0,
        "country":1,
        "year":1,
        "sex":1,
        "age":1,
        "suicides_no":1,
        "population":1,
        "suicides_per_100k":1,
        "country_year":1,
        "gdp_per_year":1,
        "gdp_per_capita":1,
        "generation":1,
    }).limit(20)

def find(hol, hol1):
    db = getDB()
    return db.rates.find({hol:hol1},{
        "_id":0,
        "country":1,
        "year":1,
        "sex":1,
        "age":1,
        "suicides_no":1,
        "population":1,
        "suicides_per_100k":1,
        "country_year":1,
        "gdp_per_year":1,
        "gdp_per_capita":1,
        "generation":1,
    }).limit(20)