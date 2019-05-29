from pymongo import MongoClient

def get_db():
    # Acceder a la base de datos
    pass

def insertar(**kwargs):
    db = get_db()
    resultado = db.rates.insert(kwargs)
    return resultado.inserted_id

"""
    updateCollecion recibe como argumentos el id de la base de datos y actCampos, dentro del método actualiza los campos del diccionario 
    sin contar el id de los datos
"""

def update(id, **actCampos):
    db = get_db()
    resultado = db.rates.update_one(
        {
           "_id":id          
        }, {
           '$set': actCampos
        })
    return resultado.modified_count


#Método de eliminar inicio de la implementación
def delete(id):
    db = get_db()
    resultado = db.rates.delete_one({"_id":id})
    return resultado.deleted_count;

