from block import Block
from blockchain import Blockchain
from transaction import Transaction
import random
import hashlib

mycoin = Blockchain()

# random users and random transactions
def rand():
    return hashlib.md5(str(random.randrange(0, 5))).hexdigest()

for i in range(0, 10):
    mycoin.addBlock(Block(Transaction(rand(), rand(), random.randrange(1, 10000)), mycoin.getMostRecentHash()))


mycoin.printBlockChain()
