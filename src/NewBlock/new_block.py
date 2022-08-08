
from src.Utils.Block import Block
from src.NewBlock.save_to_db import insert_block

from src.ReadChain.verify_chain import verify_chain_integrity
from src.ReadChain.read_chain import read_chain

def new_block(json_data):

    timestamp = json_data["timestamp"]
    event_id = json_data["event_id"]
    chain_id = json_data["radio_id"]

    chain = read_chain(chain_id)

    if not verify_chain_integrity(chain):
        return {
            "Error" : "Error in chain verification",
            "Iserted" : False
        }

    block = Block(event_id, chain_id, timestamp, chain.blocks[-1].hash_block())
    insert_block(block)

    return {
        "Error" : None,
        "Inserted": True
    }