import random
from typing import List

"""T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create an algorithm to determine if T2 is a subtree of T1.
A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2. 
That is, if you cut off the tree at node n, the two trees would be identical. """


#This one actually sounds "easy". First, look for a possible node in T1 that is the head of main node of T2. 
# If there is none, break, as T2 is not a subtree of T1. Then, just check every node and check if they are equal. 
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
            self.level = 0
            Tree.allNodes.append(self)
        def appendToTaik(self, dataVal = None, state = state.unvisited):
            end = Tree.Node(dataVal,state)
            level = 0
            n = self
            while n.nextval != None:
                n = n.nextval
                level += 1
            n.nextval = end
            end.parent = n
            end.level = level
        def binaryTree(self,nextNode,level=1):
            if type(nextNode) == int:
                node = Tree.Node(dataval=nextNode, state=state.unvisited)
                if (nextNode > self.dataval):
                    if (self.leftPath == None):
                        #self.leftPath.binaryTree(nextNode)
                        self.leftPath = node
                        node.parent = self
                        node.level = level
                    else:
                        level += 1
                        self.leftPath.binaryTree(nextNode,level=level)
                if (nextNode < self.dataval):
                    if (self.rightPath == None):
                        #self.rightPath.binaryTree(nextNode)
                        self.rightPath = node
                        node.parent = self
                        node.level = level
                    else:
                        level += 1
                        self.rightPath.binaryTree(nextNode, level=level)
            else:
                node = nextNode
                if (nextNode.dataval > self.dataval):
                    if (self.leftPath == None):
                        #self.leftPath.binaryTree(nextNode)
                        self.leftPath = node
                        node.parent = self
                        node.level = level
                    else:
                        level += 1
                        self.leftPath.binaryTree(nextNode, level=level)
                if (nextNode.dataval < self.dataval):
                    if (self.rightPath == None):
                        #self.rightPath.binaryTree(nextNode)
                        self.rightPath = node
                        node.parent = self
                        node.level = level
                    else:
                        level+=1
                        self.rightPath.binaryTree(nextNode,level=level)
        
        def printData(self):
            if self.leftPath:
                self.leftPath.printData()
            print("({},{})".format(self.dataval,self.level))
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
        roots.append(root)
        output.append(root)
    #Now, we look at the ones that are only on the left side of the dependencies list
    for proj in differenceInLists(leftSide,rightSide):
        output.append(proj)
    while dependendies:
        #Now we remove the dependencies that have been completed
        newDependencies = []
        for dependency in dependendies:
            if not (dependency[0] in output and dependency[1] in output):
                newDependencies.append(dependency)
        dependendies = newDependencies
        #Now, we take a look at the ones on the left side that depend only on the ones on the output list
        for dependency in dependendies:
            if dependency[0] in output:
                output.append(dependency[1])
            else:
                if dependency[1] in output:
                    output.remove(dependency[1])
    return output

def findCommonAncestor(node1: Tree.Node, node2: Tree.Node):
    #One way to make this work would be first get a path from one node to the first node. Store them in a hash map
    #Then do the same with the other node. Once you find the first same node, that is a common ancestor
    #But we can not do that due to the limitatino of not storing nodes in a data structure.
    #If we cannot store it, we could start from the master node, and if it were a binary search tree, 
    #just check where they diverge. 
    #But as it is not a binary search tree, do the reverse. it would be a O² but it would work. lets see
    #p = parent
    #We could add a "level" data to the nodes, that way, we can skip every node below them. 
    p1 = node1.parent
    p2 = node2.parent
    while p2.level > p1.level:
        p2 = p2.parent
    while p1.level > p2.level:
        p1 = p1.parent
    init1 = p1
    init2 = p2
    while p1 is not None:
        p2 = init2
        while p2 is not None:
            if p1.dataval == p2.dataval:
                return p1
            p2 = p2.parent
        p1 = init1
    return False

def findNodeInTree(node: Tree.Node, root: Tree.Node):
    if root:
        if node.dataval == root.dataval:
            return root
        elif node.dataval < root.dataval:
            return findNodeInTree(node, root.rightPath)
        elif node.dataval > root.dataval:
            return findNodeInTree(node, root.leftPath)

def verifySameTree(main: Tree.Node, secundary: Tree.Node):
    nodesMain = []
    nodesMain.append(main.leftPath)
    nodesMain.append(main.rightPath)
    secundaryNodes = []
    secundaryNodes.append(secundary.leftPath)
    secundaryNodes.append(secundary.rightPath)
    i = 0
    while len(nodesMain) > 0 and len(secundaryNodes) > 0:
        if nodesMain[i].dataval != secundaryNodes[i].dataval:
            return False
        nodesMain.append(nodesMain[i].leftPath)
        nodesMain.append(nodesMain[i].rightPath)
        secundaryNodes.append(secundaryNodes[i].leftPath)
        secundaryNodes.append(secundaryNodes[i].rightPath)
        i+=1
    return True

def isSubtree(tree1: Tree.Node, tree2: Tree.Node):
    nexus = findCommonAncestor(tree1, tree2)
    return verifySameTree(tree1, nexus)

if __name__ == "__main__":
    tree = Tree(8,state.unvisited)
    node1 = Tree.Node(3)
    node2 = Tree.Node(10)
    node3 = Tree.Node(1)
    node4 = Tree.Node(6)
    node5 = Tree.Node(4)
    node6 = Tree.Node(7)
    node7 = Tree.Node(14)
    node8 = Tree.Node(13)
    tree.root.binaryTree(node1)
    tree.root.binaryTree(node2)
    tree.root.binaryTree(node3)
    tree.root.binaryTree(node4)
    tree.root.binaryTree(node5)
    tree.root.binaryTree(node6)
    tree.root.binaryTree(node7)
    tree.root.binaryTree(node8)
    tree.root.printData()
    print(isSubtree(node2, node6))

