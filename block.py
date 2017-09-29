import hashlib

class Block():

    def __init__(self, transaction):
        self.transaction = transaction
        self.previousHash = "0"
        self.hash = self.computeHash()

    def computeHash(self):
        return hashlib.sha256(self.transaction.toString() + self.previousHash).hexdigest()
