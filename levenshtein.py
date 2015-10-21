# figuring out the Levenshtein distance between two strings
# you're allowed to insert, delete, and swap, and each costs 1

import itertools

# nodeTypes
ROOT = 0
DELETE = 1
INSERT = 2
SUBSTITUTION = 3
LEAF = 4

class Node():
    def __init__(self, start, target, nodeType=None):
        self.start = start
        self.target = target
        self.nodeType = nodeType

        if self.isLeaf():
            self.children = {}
            self.nodeType = LEAF
        else:
            self.children = {"delete": Node(start[:-1], target, DELETE),
                            "insert": Node(start, target[:-1], INSERT),
                            "substitution": Node(start[:-1], target[:-1], SUBSTITUTION)}

    def getMinChildCostAndPath(self):
        if self.nodeType == LEAF:
            cost = max(len(self.start), len(self.target))
            path = [self]

        else:
            allCostPaths = [child.getCost() for child in self.children.values()]
            cost, childPath = min(allCostPaths, key=lambda x:x[0])
            path = childPath

        return cost, path


    def getCost(self):
        childCost, childPath = self.getMinChildCostAndPath()
        child = childPath[0]

        if child.nodeType == LEAF:
            costAdjustment = 0

        elif child.nodeType in [DELETE, INSERT]:
            costAdjustment = 1

        elif child.nodeType == SUBSTITUTION:
            if self.start == "k":
                import pdb; pdb.set_trace()
            if self.start[-1] == self.target[-1]:
                costAdjustment = 0
            else:
                costAdjustment= 1

        path = [self] + childPath
        try:
            cost = childCost + costAdjustment
        except:
            import pdb; pdb.set_trace()

        return cost, path

    def isLeaf(self):
        return min(len(self.start), len(self.target)) == 0


string1 = "kitten"
string2 = "sitting"

string3 = "kit"
string4 = "sitg"


if __name__ == '__main__':
    #import doctest
    #doctest.testmod()
    cost, path =  Node(string3,string4,ROOT).getCost()
    print cost
    for node in path:
        print [node.start, node.target, node.getCost()[0]]

