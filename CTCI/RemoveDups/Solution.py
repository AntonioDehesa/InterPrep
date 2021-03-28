import random
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
    def appendToTaik(self, dataVal = None):
        end = Node(dataVal)
        n = self
        while n.nextval != None:
            n = n.nextval
        n.nextval = end

class SLinkedList:
    def __init__(self):
        self.headval = None

def removeDups(linkedList:SLinkedList):
    dups = {}
    n = linkedList.headval
    print("original")
    while n.nextval != None:
        print(n.dataval)
        n = n.nextval
    n = linkedList.headval
    prev = Node()
    while n.nextval != None:
        if dups.get(n.dataval,0) > 0:
            prev.nextval = n.nextval
        else:
            dups[n.dataval] = 1
            prev = n
        n = n.nextval
    print("After")
    n = linkedList.headval
    while n.nextval != None:
        print(n.dataval)
        n = n.nextval


if __name__ == "__main__":
    linkedList = SLinkedList()
    linkedList.headval = Node(10)
    for _ in range(200):
        linkedList.headval.appendToTaik(random.randint(1,100))
    removeDups(linkedList)
# Complexity: o(n) time, o(n) space