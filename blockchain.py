from block import Block
from transaction import Transaction
import hashlib

class Blockchain(object):

    def __init__(self):
        self.blockchain = [self.createGenesisBlock()]

    def createGenesisBlock(self):
        genesisBlock = Block(Transaction("", "", 0))
        return genesisBlock

    def getMostRecentHash(self):
        return self.blockchain[-1].hash

    def getHash(self, transaction, prevHash):
        return hashlib.sha256(transaction.toString() + str(prevHash)).hexdigest()

    def addBlock(self, newBlock):
        newBlock.previousHash = self.getMostRecentHash()
        newBlock.hash = newBlock.computeHash()
        self.blockchain.append(newBlock)

    def isValid(self):
        prevHash = self.blockchain[0].hash
        for blk in self.blockchain[1:]:
            if(blk.hash != blk.computeHash()):
                return False

            if(blk.previousHash != prevHash):
                return False
            prevHash = blk.hash

        return True

    def printBlockChain(self):
        for blk in self.blockchain:
            print [blk.transaction.toString(), blk.hash]
