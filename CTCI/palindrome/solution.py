import random

"""
Implement a function to check if a linked list is a palindrome
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

def isPalindrome(linkedList:SLinkedList):
    reversedList = reverseList(linkedList)
    n = linkedList.headval
    r = reversedList.headval
    while n != None and r!= None:
        if n.dataval != r.dataval:
            return False
        n = n.nextval
        r = r.nextval
    return True

if __name__ == "__main__":
    linkedList1 = SLinkedList()
    linkedList1.headval = Node(7)
    linkedList1.headval.appendToTaik(1)
    linkedList1.headval.appendToTaik(7)
    res = isPalindrome(linkedList1)
    print(res)
    assert(res == True)
    
# Complexity: o(n) time, o(1) space