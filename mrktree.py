import hashlib, json
from collections import OrderedDict

class MerkleTree:

    def __init__(self, listOfTransaction=None):
        self.listOfTransaction = listOfTransaction
        self.pastTransaction = OrderedDict()

    def createTree(self):

        tempTransaction = []
        for index in range(0, len(self.listOfTransaction), 2):

            current = self.listOfTransaction[index]

            if index + 1 != len(self.listOfTransaction):
                current_right = self.listOfTransaction[index+1]
            else:
                current_right = ''

            current_encode = current.encode('utf-8')
            current_hash = hashlib.sha256(current_encode)

            if current_right != '':
                current_right_encode = current_right.encode('utf-8')
                current_right_hash = hashlib.sha256(current_right_encode)

            self.pastTransaction[current] = current_hash.hexdigest()

            if current_right != '':
                self.pastTransaction[current_right] = current_right_hash.hexdigest()

            if current_right != '':
                tempTransaction.append(current_hash.hexdigest() + current_right_hash.hexdigest())
            else:
                tempTransaction.append(current_hash.hexdigest)

        if len(self.listOfTransaction) != 1:
            self.listOfTransaction = tempTransaction
            self.createTree()

    def getPastTransaction(self):
        return self.pastTransaction

    def getRootNode(self):
        last_key = list(self.pastTransaction.keys())[-1]
        return self.pastTransaction[last_key]

if __name__ == '__main__':

    GTree = MerkleTree()
    transaction = ['a','b','c','d']
    GTree.listOfTransaction = transaction
    GTree.createTree()
    past_transation = GTree.getPastTransaction()
    print ('Final root of the tree:', GTree.getRootNode())
    print (json.dumps(past_transation, indent=4))
    print ('_' * 50)
