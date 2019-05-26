from pymongo import MongoClient

def get_db():
    # Acceder a la base de datos
    pass

def insertar(**kwargs):
    db = get_db()
    resultado = db.rates.insert(kwargs)
    return resultado.inserted_id