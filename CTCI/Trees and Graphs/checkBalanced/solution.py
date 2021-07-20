import random

"""
Implement a function to check if a binary tree is balanced. 
For the purposes of this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one. 
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


    def __init__(self, dataval=0, state=state.unvisited) -> None:
        self.root = self.Node(dataval=dataval,state=state)

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

    def isBalancedBase(self):
        start = self.root
        if start.leftPath == None and start.rightPath == None:
            return True
        if start.leftPath != None and start.rightPath != None:
            return isBalanced(start)
        return False

def isBalanced(start: Tree.Node):
    if start.leftPath == None and start.rightPath == None:
        return True
    if start.leftPath != None and start.rightPath != None:
        return isBalanced(start.leftPath) and isBalanced(start.rightPath)
    return False


if __name__ == "__main__":
    tree = Tree(12,state.unvisited)
    node1 = Tree.Node(6)
    node2 = Tree.Node(14)
    #node3 = Tree.Node(3)
    """tree.root.binaryTree(6)
    tree.root.binaryTree(14)
    tree.root.binaryTree(3)"""
    tree.root.binaryTree(node1)
    tree.root.binaryTree(node2)
    #tree.root.binaryTree(node3)
    tree.root.printData()
    print(tree.isBalancedBase())