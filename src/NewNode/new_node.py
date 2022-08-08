
import sqlite3
from src.parameters import database_name

def new_node():
    
    #Crea un nuevo nodo y la inserta en la base de datos

    connection = sqlite3.connect(f"{database_name}.db")
    cursor = connection.cursor()

    query = """INSERT INTO NODESTATUS(node_id, estado, ultima_actualizacion)
    VALUES(?,?,?)"""

    data_touple = (0, 1, 0) #hay que definir estos valores

    cursor.execute(query, data_touple)
    connection.commit()
    connection.close()

    return True