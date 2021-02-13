from .node import Node
import time

class BlockChain:
    difficulty = 3

    def __init__(self):
        self.new_transactions = []
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Node(
            index=0,
            transactions="Genesis Block",
            previous_hash=None,
        )
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    def last_block(self):
        return self.chain[-1]

    def add_block(self, block, proof):
        previous_hash = self.last_block().hash
    
        if previous_hash != block.previous_hash:
            return False
        if not self.is_valid_proof(block, proof):
            return False
        block.hash = proof
        self.chain.append(block)
        return True

    def is_valid_proof(self, block, proof):
        return block.hash.startswith(
            '0' * BlockChain.difficulty
        )

    def mine(self):
        if not self.new_transactions:
            return False
        for transaction in self.new_transactions:
            last_block = self.last_block()
            new_block = Node(
                index=last_block.index + 1,
                transactions=transaction,
                previous_hash=last_block.hash,
            )
            proof = self.find_proof_of_work(new_block)
            self.add_block(new_block, proof)

        self.new_transactions = []
        return True

    def proof_of_work(self, block):
        computed_hash = block.compute_hash()
        while not computed_hash.startswith(
            '0' * BlockChain.difficulty
        ):
            block.nonce += 1
            computed_hash = block.compute_hash()
        return computed_hash
    

    def chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1

        while block_index < len(chain):
            block = chain[block_index]
            if block["previous_hash"] != previous_block.compute_hash():
                return False
            proof = block["proof"]
            if not self.is_valid_proof(block, proof):
                return False
            previous_block = block
            block_index += 1
        return True