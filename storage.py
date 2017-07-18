from typing import Optional, List
from copy import deepcopy

import hashlib
import time


# Class to store the blocks information
class Block:
    def __init__(self, number, previous_hash, data):
        self.number = number
        self.previous_hash = previous_hash
        self.data = data
        self.nonce = 0
        self.timestamp = time.time()
        self.block_hash = ""


def calculate_hash(block: Block) -> str:
    return hashlib.sha256("{}{}{}{}{}".format(
        block.number,
        block.previous_hash,
        block.data,
        block.nonce,
        block.timestamp
    ).encode('utf_8')).hexdigest()


def mine(block: Block, prefix: str) -> Optional[Block]:
    nonce = 0
    print("Mining...")
    while True:
        block.nonce = nonce
        block_hash = calculate_hash(block)
        print(block_hash)
        if block_hash.startswith(prefix):
            block.block_hash = block_hash
            return block
        nonce += 1

    return None


def generate_genesis(prefix) -> Block:
    return mine(Block(number=0, previous_hash="0", data="Genesis block"), prefix)


def validate_blockchain(blockchain):
    idx = -1
    block = blockchain[-1]
    while True:
        try:
            # Genesis found
            if block.previous_hash == "0":
                return True
            # Ooops, invalid blockchain
            elif block.previous_hash != blockchain[idx - 1].block_hash:
                return False
        except IndexError:
            return False
        idx -= 1

    return False


def is_valid_block(previous_block: Block, block: Block, prefix: str) -> bool:
    if previous_block.number + 1 != block.number:
        return False
    if previous_block.block_hash != block.previous_hash:
        return False
    if not previous_block.block_hash.startswith(prefix):
        return False
    if previous_block.timestamp > block.timestamp:
        return False

    return True


def add_to_blockchain(blockchain: List[Block], block: Block) -> List[Block]:
    blockchain_copied = deepcopy(blockchain)
    if is_valid_block(blockchain[-1], block, prefix="00"):
        blockchain_copied.append(block)
    return blockchain_copied


def longest_blockchain(blockchain: List[Block], new_blockchain: List[Block]):
    if len(new_blockchain) > len(blockchain):
        blockchain = new_blockchain
    return blockchain
