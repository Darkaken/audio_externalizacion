
import sqlite3
from src.parameters import database_name

def modify_stats(node_id, audios_analizados, tandas_encontradas):

    if audios_analizados < tandas_encontradas:
        raise Exception("Se econtraron mas tandas de las que se analizaron")

    connection = sqlite3.connect(f"{database_name}.db")
    cursor = connection.cursor()

    query = None  # UPDATE BDD

    data_touple = (node_id, audios_analizados, tandas_encontradas)  # Datos para updatear

    cursor.execute(query, data_touple)
    connection.commit()
    connection.close()