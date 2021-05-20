import random

"""
Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node.
Note that the intersection is defined based on reference, not value. 
That is, if the kth node of the first linked list is the exact same node (by reference) as the jth node of the second linked list, 
then they are intersecting. 
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

def reverseList(linkedList:SLinkedList):
    newList = SLinkedList()
    n = linkedList.headval
    while n != None:
        a = Node(n.dataval)
        a.nextval = newList.headval
        newList.headval = a
        n = n.nextval
    n = linkedList.headval
    while n!=None:
        print("{}->".format(n.dataval))
        n = n.nextval
    n = newList.headval
    while n!=None:
        print("{}->".format(n.dataval))
        n = n.nextval
    return newList


"""
Explanation: we first check the last node of each list. if they are different, then the lists dont intersect. 
If they are the same, we need to find out where they intersect. 
For this, we need to know the difference in length, if any. 
Afterwards, we advance in the longest list, and once we are at the "same length", we can compare each node, and see where they are the same. 
"""
def intersection(linkedList1:SLinkedList, linkedList2:SLinkedList):
    n1 = linkedList1.headval
    l1 = 0
    while n1.nextval != None:
        l1+=1
        n1 = n1.nextval
    n2 = linkedList2.headval
    l2 = 0
    while n2.nextval != None:
        l2+=1
        n2 = n2.nextval
    if n1 != n2:
        return False,None
    n1 = linkedList1.headval
    n2 = linkedList2.headval
    if l1>l2:
        for _ in range(l1-l2):
            n1 = n1.nextval
    else:
        for _ in range(l2-l1):
            n2 = n2.nextval
    while n1 != None and n2!=None and n1 != n2:
        n1 = n1.nextval
        n2 = n2.nextval
    return True,n1

if __name__ == "__main__":
    linkedList1 = SLinkedList()
    linkedList1.headval = Node(3)
    linkedList1.headval.appendToTaik(1)
    linkedList1.headval.appendToTaik(5)
    linkedList1.headval.appendToTaik(9)
    linkedList1.headval.appendToTaik(7)
    linkedList1.headval.appendToTaik(2)
    linkedList1.headval.appendToTaik(1)
    linkedList2 = SLinkedList()
    linkedList2.headval = Node(4)
    linkedList2.headval.appendToTaik(6)
    linkedList2.headval.appendToTaik(7)
    linkedList2.headval.appendToTaik(2)
    linkedList2.headval.appendToTaik(1)

    res = intersection(linkedList1,linkedList2)
    print(res[0])
    assert(res[0] == False)

    linkedList1 = SLinkedList()
    linkedList1.headval = Node(3)
    linkedList1.headval.appendToTaik(1)
    linkedList1.headval.appendToTaik(5)
    linkedList1.headval.appendToTaik(9)
    linkedList2 = SLinkedList()
    linkedList2.headval = Node(4)
    linkedList2.headval.appendToTaik(6)
    nodea = Node(7)
    nodeb = Node(2)
    nodec = Node(1)
    nodea.nextval = nodeb
    nodeb.nextval = nodec
    n = linkedList1.headval
    while n.nextval != None:
        n = n.nextval
    n.nextval = nodea
    n = linkedList2.headval
    while n.nextval != None:
        n = n.nextval
    n.nextval = nodea

    res = intersection(linkedList1,linkedList2)
    print(res[0])
    assert(res[0] == True)
    print("Intersection: {}".format(res[1].dataval))