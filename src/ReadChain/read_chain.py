

import sqlite3
from src.parameters import database_name
from src.Utils.Chain import Chain
from src.Utils.Block import Block

def read_chain(chain_id):

    connector = sqlite3.connect(f"{database_name}.db")
    cursor = connector.cursor()

    query = """SELECT * FROM MAIN WHERE chain_id = ?"""

    cursor.execute(query, (chain_id,))
    result = cursor.fetchall()

    chain = Chain()

    for block in result:

        temp = Block(block[2], block[1], block[0], block[3])
        chain.add_block(temp)

    return chain