# Simple Blockchain Simulation

This project is a basic blockchain simulation written in Python. It demonstrates the fundamental concepts of a blockchain, including block structure, cryptographic hashing, proof-of-work, and chain validation. The simulation also includes a tampering mechanism to show how data integrity is maintained.

## Features

- **Block Structure:** Each block contains an index, timestamp, a list of transactions, the hash of the previous block, a nonce, and its own hash.
- **Hashing:** Uses the SHA-256 algorithm to compute the hash of each block based on its contents.
- **Blockchain Management:** A `Blockchain` class that handles block creation, chain integrity verification, and appending new blocks.
- **Proof-of-Work:** A simple proof-of-work mechanism that requires the block hash to start with a specified number of zeros (difficulty).
- **Tamper Detection:** A method to intentionally tamper with block data, demonstrating how the blockchain validation detects inconsistencies.

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

- **Python 3.x**  
  Make sure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/blockchain-simulation.git
   ```
2. **Navigate to the Project Directory**

   ```bash
   cd blockchain-simulation
   ```
3. **Running the Simulation**

Run the simulation by executing the Python script:

   ```bash
   python run.py
   ```

## Result:

The script will:

- Create a genesis block.
- Add new blocks with dummy transactions.
- Display the blockchain's state.
- Validate the blockchain's integrity.
- Tamper with a block and demonstrate that the validation process can detect the tampering.
