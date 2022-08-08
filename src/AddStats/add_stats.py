import sqlite3
from src.parameters import database_name

def add_stats(node_id, tanda_encontrada = False):

    if tanda_encontrada:
        tanda_encontrada = 1
    else:
        tanda_encontrada = 0

    connection = sqlite3.connect(f"{database_name}.db")
    cursor = connection.cursor()

    query = None #UPDATE BDD

    data_touple = (node_id, 1, tanda_encontrada) #Datos para updatear

    cursor.execute(query, data_touple)
    connection.commit()
    connection.close()
