import random

"""
Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. 
If x is contained withing the list, the values of x only need to be after the elements less than x (see below). The partition element x can appear anuwhere 
in the "right partition"; it does not need to appear between the left and right partitions. 
Example
Input: 3->5->8->5->10->2->1[Partition 5]
Output: 3->1->2->10->5->5->8
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

def partition(linkedList:SLinkedList, k:int):
    print("Print before")
    n = linkedList.headval
    while n.nextval != None:
        print("{} ->".format(n.dataval))
        n = n.nextval
    n = linkedList.headval
    listBefore = None
    listAfter = None
    listMid = None
    while n.nextval != None:
        #print("Valor de nodo: {}".format(n.dataval))
        if n.dataval < k:
            #print("It is minor")
            if listBefore == None:
                listBefore = SLinkedList()
                listBefore.headval = Node(n.dataval)
            else:
                listBefore.headval.appendToTaik(n.dataval)
        elif n.dataval == k:
            #print("It is the same")
            if listMid == None:
                listMid = SLinkedList()
                listMid.headval = Node(n.dataval)
            else:
                listMid.headval.appendToTaik(n.dataval)
        else:
            #print("It is over")
            if listAfter == None:
                listAfter = SLinkedList()
                listAfter.headval = Node(n.dataval)
            else:
                listAfter.headval.appendToTaik(n.dataval)
        n = n.nextval
    a = listMid.headval
    while a.nextval != None:
        a = a.nextval
    a.nextval = listAfter.headval
    b = listBefore.headval
    while b.nextval != None:
        b = b.nextval
    b.nextval = listMid.headval
    n = listBefore.headval
    print("Print after")
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
    partition(linkedList,5)
# Complexity: o(n) time, o(1) space