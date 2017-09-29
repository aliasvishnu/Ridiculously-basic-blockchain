from block import Block
from transaction import Transaction
import hashlib

class Blockchain(object):

    def __init__(self):
        self.blockchain = [self.createGenesisBlock()]

    def createGenesisBlock(self):
        genesisBlock = Block(Transaction("", "", 0), "0")
        return genesisBlock

    def getMostRecentHash(self):
        return self.blockchain[-1].hash

    def addBlock(self, newBlock):
        newBlock.hash = hashlib.sha256(newBlock.transaction.toString() + str(self.getMostRecentHash)).hexdigest()
        self.blockchain.append(newBlock)

    def printBlockChain(self):
        for blk in self.blockchain:
            print [blk.transaction.toString(), blk.hash]
