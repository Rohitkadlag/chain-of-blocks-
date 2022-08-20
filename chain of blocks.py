import datetime

import hashlib


class Block:
    blockNo = 0

    data = None

    next = None

    hash = None

    previous_hash = 0x0

    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data

    def hash(self):
        h = hashlib.sha256()

        h.update(

            str(self.data).encode('utf-8') +

            str(self.previous_hash).encode('utf-8') +

            str(self.timestamp).encode('utf-8') +

            str(self.blockNo).encode('utf-8')

        )

        return h.hexdigest()

    def __str__(self):
        return "Block Hash: " + str(self.hash()) + "\nBlock No.: " + str(self.blockNo) + "\nBlock Data: " + str(
            self.data) + "\nPrevious hash: " + str(self.previous_hash) + "\n--------------"


class Blockchain:
    print("For Genesis block")

    block = Block(input("Enter transaction data:"))

    head = block

    def add(self, block, data):
        block.previous_hash = self.block.hash()

        block.blockNo = self.block.blockNo + 1

        block.data = data

        self.block.next = block

        self.block = self.block.next

    def mine(self, block, data):
        self.add(block, data)


blockchain = Blockchain()

for n in range(3):
    print("For block ", n + 1)

    data = input("Enter transaction data:")

    blockchain.mine(Block("Block " + str(n + 1)), data)

print("\n--------------")

while blockchain.head != None:
    print(blockchain.head)

    blockchain.head = blockchain.head.next

