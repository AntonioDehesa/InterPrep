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


if __name__ == "__main__":
    tree = Tree(12,state.unvisited)
    tree.root.binaryTree(6)
    tree.root.binaryTree(14)
    tree.root.binaryTree(3)
    tree.root.printData()
    nodes = tree.getAllNodes()
    for i in range(len(nodes)):
        print(nodes[i].dataval)
    print("nein")