import random
from typing import List

"""You are given a list of projects and a list of dependencies 
(which is a list of pairs of projects, where the second project is dependent on the first project).
All of a project's dependencies must be built before the project is. Find a build order that will allow the projects to be built. 
If there is no balid build order, return an Error
Example:
Input:
    projects: a,b,c,d,e,f
    dependencies: (a,d), (f,b), (b,d), (f,a), (d,c)
Output: f,e,a,b,d,c"""

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
            self.parent = None
            self.state = state.unvisited
            Tree.allNodes.append(self)
        def appendToTaik(self, dataVal = None, state = state.unvisited):
            end = Tree.Node(dataVal,state)
            n = self
            while n.nextval != None:
                n = n.nextval
            n.nextval = end
            end.parent = n
        def binaryTree(self,nextNode):
            if type(nextNode) == int:
                node = Tree.Node(dataval=nextNode, state=state.unvisited)
                if (nextNode > self.dataval):
                    if (self.leftPath == None):
                        #self.leftPath.binaryTree(nextNode)
                        self.leftPath = node
                        node.parent = self
                    else:
                        self.leftPath.binaryTree(nextNode)
                if (nextNode < self.dataval):
                    if (self.rightPath == None):
                        #self.rightPath.binaryTree(nextNode)
                        self.rightPath = node
                        node.parent = self
                    else:
                        self.rightPath.binaryTree(nextNode)
            else:
                node = nextNode
                if (nextNode.dataval > self.dataval):
                    if (self.leftPath == None):
                        #self.leftPath.binaryTree(nextNode)
                        self.leftPath = node
                        node.parent = self
                    else:
                        self.leftPath.binaryTree(nextNode)
                if (nextNode.dataval < self.dataval):
                    if (self.rightPath == None):
                        #self.rightPath.binaryTree(nextNode)
                        self.rightPath = node
                        node.parent = self
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
    
    def isEmpty(self):
        return not self.getAllNodes

def isBalanced(start: Tree.Node):
    if start.leftPath == None and start.rightPath == None:
        return True
    if start.leftPath != None and start.rightPath != None:
        return isBalanced(start.leftPath) and isBalanced(start.rightPath)
    return False


def validateBSTMain(tree: Tree):
    validation = {}
    if tree.isEmpty():
        return True
    return validateBST(tree.root, validation)

def validateBST(tree: Tree.Node, validation):
    if not tree:
        return True
    if tree.dataval in validation:
        return False
    else:
        validation[tree.dataval] = 1
    if tree.leftPath:
        if tree.leftPath.dataval <= tree.dataval:
            return False
    if tree.rightPath:
        if tree.rightPath.dataval >= tree.dataval:
            return False
    return validateBST(tree.rightPath,validation) and validateBST(tree.leftPath,validation)
    
def returnNextNode(node: Tree.Node):
    if node:
        if node.rightPath:
            n = node.rightPath
            while n.leftPath:
                n = n.leftPath
            return n
        elif node.leftPath:
            return returnNextNode(node.leftPath)
        else:
            q = node
            x = q.parent
            while x != None and x.leftPath != q:
                q = x
                x = x.parent
            return x
    return None

def differenceInLists(l1: List, l2: List):
    #return list(set(l1) - set(l2)) + list(set(l2) - set(l1))
    result = []
    for project in l1:
        if project not in l2:
            result.append(project)
    return result

def checkDependencies(projects: list, dependendies: list):
    #First we deflate the dependencies
    deflatedDependencies = []
    leftSide = []
    rightSide = []
    for dependency in dependendies:
        if dependency[0] not in leftSide:
            leftSide.append(dependency[0])
        if dependency[1] not in rightSide:
            rightSide.append(dependency[1])
        for proj in dependency:
            if proj not in deflatedDependencies:
                deflatedDependencies.append(proj)
    #Now we add the ones who are independent to the roots list
    output = []
    roots = []
    for root in differenceInLists(projects, deflatedDependencies):
    #for root in (list(set(projects) - set(deflatedDependencies)) + list(set(deflatedDependencies) - set(projects))):
    #for root in (projects - deflatedDependencies):
        roots.append(root)
        output.append(root)
    #    roots[root] = Tree.node(ord(root))
    #Now, we look at the ones that are only on the left side of the dependencies list
    for proj in differenceInLists(leftSide,rightSide):
    #for proj in (leftSide- rightSide):
        output.append(proj)
    while dependendies:
        #Now we remove the dependencies that have been completed
        newDependencies = []
        for dependency in dependendies:
            if not (dependency[0] in output and dependency[1] in output):
                newDependencies.append(dependency)
        dependendies = newDependencies
        #Now, we take a look at the ones on the left side that depend only on the ones on the output list
        #toAdd = []
        for dependency in dependendies:
            if dependency[0] in output:
                output.append(dependency[1])
                #toAdd.append(dependency[1])
            else:
                #toAdd.remove(dependency[1])
                if dependency[1] in output:
                    output.remove(dependency[1])
    return output

if __name__ == "__main__":
    """tree = Tree(8,state.unvisited)
    node1 = Tree.Node(3)
    node2 = Tree.Node(10)
    node3 = Tree.Node(1)
    node4 = Tree.Node(6)
    node5 = Tree.Node(4)
    node6 = Tree.Node(7)
    node7 = Tree.Node(14)
    node8 = Tree.Node(13)
    node9 = Tree.Node(13)
    tree.root.binaryTree(node1)
    tree.root.binaryTree(node2)
    tree.root.binaryTree(node3)
    tree.root.binaryTree(node4)
    tree.root.binaryTree(node5)
    tree.root.binaryTree(node6)
    tree.root.binaryTree(node7)
    tree.root.binaryTree(node8)
    tree.root.binaryTree(node9)
    tree.root.printData()
    print(returnNextNode(node8).dataval)"""
    projects = ["a","b","c","d","e","f","g"]
    dependencies = [["a","d"],["f","b"],["b","d"],["f","a"],["d","c"],["e","g"]]
    print(checkDependencies(projects=projects, dependendies=dependencies))
    #Example two
