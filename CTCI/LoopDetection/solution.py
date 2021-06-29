import random

"""
Given a circular linked list, implement an algorith that returns the node at the beginning of the loop
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

def loopDetection(linkedList:SLinkedList):
    slow = linkedList.headval
    fast = linkedList.headval
    print("Slow: {}".format(slow.dataval))
    print("Fast: {}".format(fast.dataval))
    while slow.nextval != None and fast.nextval.nextval != None:
        slow = slow.nextval
        fast = fast.nextval.nextval
        print("Slow: {}".format(slow.dataval))
        print("Fast: {}".format(fast.dataval))
        if slow == fast:
            return slow#It returns any immediate node that repeats itself
    return False

if __name__ == "__main__":
    linkedList = SLinkedList()
    linkedList.headval = Node(1)
    linkedList.headval.appendToTaik(2)
    node3 = Node(3)
    n = linkedList.headval
    while n.nextval != None:
        n = n.nextval
    n.nextval = node3
    linkedList.headval.appendToTaik(4)
    linkedList.headval.appendToTaik(5)
    while n.nextval != None:
        n = n.nextval
    n.nextval = node3

    """while n.nextval != None:
        print(n.dataval)
        n = n.nextval"""

    res = loopDetection(linkedList)
    if type(res) == bool:
        print(res)
    else:
        print(res.dataval)