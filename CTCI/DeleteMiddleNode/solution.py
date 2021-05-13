import random

"""
implement an algorith to delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list,
given only access to that node
Example: 
Input: the node c from the linked list a->b->c->d->e->f
Output: nothing is returned, but the new linked list looks like a->b->d->e->f
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

def deleteMid(linkedList:SLinkedList, k:int):
    n = linkedList.headval
    if n.dataval == k:
        print("You cannot delete the first element")
        return None
    while n.nextval != None:
        print("{} ->".format(n.dataval))
        n = n.nextval
    n = linkedList.headval
    while n.nextval != None:
        if n.nextval.dataval == k:
            n.nextval = n.nextval.nextval
            break
        n = n.nextval
    n = linkedList.headval
    print("After deleting")
    while n.nextval != None:
        print("{} ->".format(n.dataval))
        n = n.nextval

if __name__ == "__main__":
    linkedList = SLinkedList()
    linkedList.headval = Node(10)
    for _ in range(9):
        linkedList.headval.appendToTaik(random.randint(1,20))
    linkedList.headval.appendToTaik(5)
    for _ in range(10):
        linkedList.headval.appendToTaik(random.randint(1,20))
    deleteMid(linkedList,5)
# Complexity: o(n) time, o(1) space