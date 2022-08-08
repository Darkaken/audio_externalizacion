
class Chain(object):
    def __init__(self):

        self.blocks = []

    def validate_blockchain(self):

        for index in range(1, len(self.blocks) - 1):
            if self.blocks[index].prev_hash != self.blocks[index - 1].hash_block():
                return False
        return True

    def recompute_blockchain(self): #we need to make this function impossible to be executed

        for index in range(1, len(self.blocks) - 1):
            self.blocks[index].prev_hash = self.blocks[index - 1].hash_block()

    def add_block(self, block):
        self.blocks.append(block)

    def get_length(self):
        return len(self.blocks)

