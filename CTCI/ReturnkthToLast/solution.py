import random

"""
implement an algorith to find the kth to last element of a singly linked list
"""

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

def findkth(linkedList:SLinkedList, k:int):
    dups = {}
    n = linkedList.headval
    while n.nextval != None:
        print(n.dataval)
        n = n.nextval
    n = linkedList.headval
    future = linkedList.headval
    for i in range(k):
        if future.nextval != None:
            future = future.nextval
        else:
            print("Not possible. Not enough elements")
            break
    while future.nextval != None:
        n = n.nextval
        future = future.nextval
    print(n.dataval)

if __name__ == "__main__":
    linkedList = SLinkedList()
    linkedList.headval = Node(10)
    for _ in range(200):
        linkedList.headval.appendToTaik(random.randint(1,100))
    findkth(linkedList, 5)
# Complexity: o(n) time, o(1) space