import hashlib
import json
from datetime import datetime
from Block import Block


class Blockchain:
    difficulty = 3

    def __init__(self):
        """
        Initialize the blockchain by creating the genesis block.
        """
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Generates the genesis (first) block and appends it to the chain.
        The genesis block has an index of 0 and a previous_hash of '0'.
        """
        genesis_block = Block(
            0, ["Genesis Block"], datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "0"
        )
        genesis_block.hash = self.proof_of_work(genesis_block)
        self.chain.append(genesis_block)

    def add_new_block(self, transactions):
        """
        Creates a new block with the provided transactions and adds it to the blockchain.
        """
        index = len(self.chain)
        previous_hash = self.chain[-1].hash
        new_block = Block(
            index,
            transactions,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            previous_hash,
        )
        # Run the proof-of-work algorithm to get a valid hash.
        new_block.hash = self.proof_of_work(new_block)
        self.chain.append(new_block)

    def proof_of_work(self, block):
        """
        Simple Proof-of-Work (PoW) algorithm:
        Increment the nonce until the block's hash has the required number of leading zeros.
        """
        block.nonce = 0
        computed_hash = block.compute_hash()
        # Loop until the computed hash satisfies the difficulty condition.
        while not computed_hash.startswith("0" * Blockchain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()
        return computed_hash

    def is_chain_valid(self):
        """
        Check the integrity of the blockchain:
        - Each block's stored hash must match its computed hash.
        - Each block's previous_hash must equal the hash of the previous block.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            # Recompute the hash and compare with the stored hash.
            if current_block.hash != current_block.compute_hash():
                print(
                    f"Block {current_block.index} has been tampered with (hash mismatch)."
                )
                return False
            # Compare the previous_hash of the current block with the hash of the previous block.
            if current_block.previous_hash != previous_block.hash:
                print(
                    f"Block {current_block.index} previous hash doesn't match the hash of block {previous_block.index}."
                )
                return False
        return True


def tamper_with_block(blockchain, index, new_transactions):
    """
    Tamper with the data of a block at a given index.
    Note: This function deliberately changes the block data without re-mining it, so chain validation should fail.
    """
    if index < len(blockchain.chain):
        print(f"\n[!] Tampering with Block {index}...")
        blockchain.chain[index].transactions = new_transactions
        # Recompute the hash without doing the proof-of-work, which will likely invalidate the chain.
        blockchain.chain[index].hash = blockchain.chain[index].compute_hash()
    else:
        print(f"No block exists at index {index} to tamper with.")


def print_blockchain(blockchain):
    """
    Print the details of each block in the blockchain.
    """
    for block in blockchain.chain:
        print(f"Block #{block.index}")
        print(f" Timestamp      : {block.timestamp}")
        print(f" Transactions   : {block.transactions}")
        print(f" Previous Hash  : {block.previous_hash}")
        print(f" Nonce          : {block.nonce}")
        print(f" Hash           : {block.hash}\n")
    print("=" * 60)


def main():

    blockchain = Blockchain()

    # Add new blocks with dummy transactions.
    blockchain.add_new_block(["Alice pays Bob 10 BTC", "Bob pays Charlie 5 BTC"])
    blockchain.add_new_block(["Charlie pays Dave 3 BTC", "Dave pays Eve 1 BTC"])

    print("Initial Blockchain State:")
    print_blockchain(blockchain)

    # Validate the blockchain before tampering.
    print("Blockchain valid?", blockchain.is_chain_valid())

    # Tamper with block 1 (the second block in the chain).
    tamper_with_block(blockchain, 1, ["Alice pays Bob 1000 BTC"])

    print("\nBlockchain State After Tampering:")
    print_blockchain(blockchain)

    # Validate the blockchain after tampering.
    print("Blockchain valid?", blockchain.is_chain_valid())


if __name__ == "__main__":
    main()
