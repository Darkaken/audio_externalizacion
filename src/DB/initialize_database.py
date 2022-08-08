
import sqlite3
from src.parameters import database_name

def create_database(db_name):
    connection = sqlite3.connect(f"{db_name}.db") #crea la base de datos
    connection.commit() #guarda el archivo .db

def create_event_table(db_name):

    connection = sqlite3.connect(f"{db_name}.db")
    cursor = connection.cursor()

    table = """CREATE TABLE MAIN (
        timestamp VARCHAR(50) NOT NULL,
        chain_id INTEGER NOT NULL,
        event_id INTEGER NOT NULL,
        prev_hash VARCHAR(255) NOT NULL
    );"""

    cursor.execute(table)
    connection.close()

    return True

def create_sys_info_table(db_name):

    connection = sqlite3.connect(f"{db_name}.db")
    cursor = connection.cursor()

    table = """CREATE TABLE NODEINFO(
        node_id INTEGER NOT NULL,
        audios_analizados INTEGER NOT NULL,
        tandas_encontradas INTEGER NOT NULL
    );"""

    cursor.execute(table)
    connection.close()

    return True

def create_node_status_table(db_name):

    connection = sqlite3.connect(f"{db_name}.db")
    cursor = connection.cursor()

    table = """CREATE TABLE NODESTATUS(
        node_id INTEGER NOT NULL,
        estado INTEGER NOT NULL,
        ultima_actualizacion TIMESTAMP NOT NULL
    );"""

    cursor.execute(table)
    connection.close()

    return True

if __name__ == '__main__':

    create_database(database_name)
    create_event_table(database_name)
    create_sys_info_table(database_name)
    create_node_status_table(database_name)

