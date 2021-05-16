import random

"""
You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit
is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.
Example
Input: 
(7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295
Output: 2-> 1 -> 9. That is, 912
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

def addSum(linkedList1:SLinkedList, linkedList2:SLinkedList):
    multi = 1
    number1 = 0
    n = linkedList1.headval
    while n != None:
        number1+= n.dataval*multi
        multi*=10
        n = n.nextval
    multi = 1
    number2 = 0
    n = linkedList2.headval
    while n != None:
        number2+= n.dataval*multi
        multi*=10
        n = n.nextval
    print(number1)
    print(number2)
    res = number1 + number2
    print(res)
    digits = [int(x) for x in str(res)[::-1]]
    result = SLinkedList()
    result.headval = Node(digits.pop(0))
    for digit in digits:
        result.headval.appendToTaik(digit)
    n = result.headval
    while n != None:
        print(n.dataval)
        n = n.nextval
    return result

if __name__ == "__main__":
    linkedList1 = SLinkedList()
    linkedList1.headval = Node(7)
    linkedList1.headval.appendToTaik(1)
    linkedList1.headval.appendToTaik(6)
    linkedList2 = SLinkedList()
    linkedList2.headval = Node(5)
    linkedList2.headval.appendToTaik(9)
    linkedList2.headval.appendToTaik(2)
    res = addSum(linkedList1, linkedList2)
    n = res.headval
    while n != None:
        print(n.dataval)
        n = n.nextval
    
# Complexity: o(n) time, o(1) space