import hashlib
import json
from datetime import datetime


class Block:
    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0):
        """
        Initialize a new block in the blockchain.
        """
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.compute_hash()

    def compute_hash(self):
        """
        Returns the SHA-256 hash of the block contents.
        We create a dictionary of the block data (excluding the hash itself) and then hash its JSON representation.
        """
        block_data = {
            "index": self.index,
            "transactions": self.transactions,
            "timestamp": self.timestamp,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce,
        }
        block_string = json.dumps(block_data, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()
