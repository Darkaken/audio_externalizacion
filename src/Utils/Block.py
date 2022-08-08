
from src.Utils.hashfunction import hash_data

class Block(object):
    def __init__(self, event_id, chain_id, timestamp, prev_hash):

        self.event_id = event_id
        self.chain_id = self.chain_id_formatting(chain_id)
        self.timestamp = self.date_formatting(timestamp)
        self.prev_hash = prev_hash #hexadecimal format

    def hash_block(self):

        to_hash = f"{self.event_id} {self.chain_id} {self.timestamp} {self.prev_hash}".encode("UTF-8")
        return hash_data(to_hash).hexdigest()

    def display(self):

        print(f"time: {self.timestamp} chain: {self.chain_id} event: {self.event_id} prev_hash: {self.prev_hash} myhash: {self.hash_block()}")

    @staticmethod
    def date_formatting(timestamp):

        # Timestamps will have the following format: str(yyyy-mm-dd hh:mm:ss) for hash calculation

        return timestamp

    @staticmethod
    def chain_id_formatting(chain_id):

        return chain_id



