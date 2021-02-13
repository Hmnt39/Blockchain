import json
from hashlib import sha256
import time

class Node:

    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()

    
    def compute_hash(self):
        block_node = json.dumps(self.__dict__).encode()
        return sha256(block_node).hexdigest()

    