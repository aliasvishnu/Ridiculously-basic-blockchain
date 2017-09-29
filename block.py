import hashlib

class Block():

    def __init__(self, transaction, previousHash):
        self.transaction = transaction
        self.hash = self.computeHash(previousHash)

    def computeHash(self, previousHash):
        return hashlib.sha256(self.transaction.toString() + previousHash).hexdigest()
