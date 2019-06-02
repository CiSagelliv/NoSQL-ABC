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

"""
    updateCollecion recibe como argumentos el id de la base de datos y actCampos, dentro del método actualiza los campos del diccionario 
    sin contar el id de los datos
"""

def update(id, **actCampos):
    db = getDB()
    resultado = db.rates.update_one(
        {
           "_id":id          
        }, {
           '$set': actCampos
        })
    return resultado.modified_count


# Método de eliminar inicio de la implementación
def delete(country,sex,age,generation):
    db = getDB()
    resultado = db.rates.delete_one({"country":country,"sex":sex,"age":age,"generation":generation})
    return resultado.deleted_count;
#No me funciono este metodo si alguien le quiere sacar provecho adelante
"""def selectOne(country,sex,age,generation):
    db=getDB()
    reg=db.rates.find_one({"country":country,"sex":sex,"age":age,"generation":generation},{"_id":1})
    return reg"""

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
        "gdp_per_capita":1,
        "generation":1,
    }).limit(20)