
import sqlite3
from src.parameters import database_name

def insert_block(Block):

    connection = sqlite3.connect(f"{database_name}.db")
    cursor = connection.cursor()

    query = """INSERT INTO MAIN(timestamp,chain_id,event_id,prev_hash)
    VALUES(?,?,?,?)"""

    data_touple = (Block.timestamp, Block.chain_id, Block.event_id, Block.prev_hash)

    cursor.execute(query, data_touple)
    connection.commit()
    connection.close()

