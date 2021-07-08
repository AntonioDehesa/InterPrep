import random

"""
Given a circular linked list, implement an algorith that returns the node at the beginning of the loop
"""

from enum import Enum

class state(Enum): 
    unvisited = 1
    visited = 2
    visiting = 3


class Tree:
    allNodes = []
    class Node:
        def __init__(self, dataval=None,state=state.unvisited):
            self.dataval = dataval
            self.leftPath = None
            self.rightPath = None
            self.state = state.unvisited
            Tree.allNodes.append(self)
        def appendToTaik(self, dataVal = None, state = state.unvisited):
            end = Tree.Node(dataVal,state)
            n = self
            while n.nextval != None:
                n = n.nextval
            n.nextval = end
        def binaryTree(self,nextNode):
            if type(nextNode) == int:
                node = Tree.Node(dataval=nextNode, state=state.unvisited)
                if (nextNode > self.dataval):
                    if (self.leftPath == None):
                        #self.leftPath.binaryTree(nextNode)
                        self.leftPath = node
                    else:
                        self.leftPath.binaryTree(nextNode)
                if (nextNode < self.dataval):
                    if (self.rightPath == None):
                        #self.rightPath.binaryTree(nextNode)
                        self.rightPath = node
                    else:
                        self.rightPath.binaryTree(nextNode)
            else:
                node = nextNode
                if (nextNode.dataval > self.dataval):
                    if (self.leftPath == None):
                        #self.leftPath.binaryTree(nextNode)
                        self.leftPath = node
                    else:
                        self.leftPath.binaryTree(nextNode)
                if (nextNode.dataval < self.dataval):
                    if (self.rightPath == None):
                        #self.rightPath.binaryTree(nextNode)
                        self.rightPath = node
                    else:
                        self.rightPath.binaryTree(nextNode)
        
        def printData(self):
            if self.leftPath:
                self.leftPath.printData()
            print(self.dataval)
            if self.rightPath:
                self.rightPath.printData()


    def __init__(self, dataval, state) -> None:
        self.root = self.Node(dataval=0,state=state.unvisited)

    def getAllNodes(self):
        return self.allNodes
    
    def routeBetweenNodes(self, start: Node, end: Node):
        if start == end:
            return True
        
        for node in self.allNodes:
            node.state = state.unvisited
        q = []

        start.state = state.visiting

        q.append(start)
        u = Tree.Node()
        while q:
            u = q.pop(0)
            if u:
                for v in [u.leftPath, u.rightPath]:
                    if v.state == state.unvisited:
                        if v == end:
                            return True
                        else:
                            v.state = state.visiting
                            q.append(v)
        return False
    
def createMinBSMain(arr):
    return createMinBST(arr, 0, len(arr) - 1)
    
def createMinBST(arr, start, end):
    if end < start:
        return None
    middle = (start+end) // 2
    midNode = Tree.Node(dataval=arr[middle])
    midNode.leftPath = createMinBST(arr, start, middle-1)
    midNode.rightPath = createMinBST(arr, middle+1, end)
    return midNode
        

def printNode(root):
    print("Left")
    if root.leftPath != None:
        printNode(root.leftPath)
    print("Print middle")
    print(root.dataval)
    print("Right")
    if root.rightPath != None:
        printNode(root.rightPath)


if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9]
    n = createMinBSMain(arr)
    print("Left")
    if n.leftPath != None:
        printNode(n.leftPath)
    print("Print middle")
    print(n.dataval)
    print("Right")
    if n.rightPath != None:
        printNode(n.rightPath)
    #print(n)
    """tree = Tree(12,state.unvisited)
    node1 = Tree.Node(6)
    node2 = Tree.Node(14)
    node3 = Tree.Node(3)
    tree.root.binaryTree(6)
    tree.root.binaryTree(14)
    tree.root.binaryTree(3)
    tree.root.binaryTree(node1)
    tree.root.binaryTree(node2)
    tree.root.binaryTree(node3)
    tree.root.printData()
    nodes = tree.getAllNodes()
    for i in range(len(nodes)):
        print(nodes[i].dataval)
    print("nein")
    print(tree.routeBetweenNodes(node1,node3))"""