# figuring out the Levenshtein distance between two strings
# you're allowed to insert, delete, and swap, and each costs 1

import itertools

# nodeTypes
ROOT = 0
DELETE = 1
INSERT = 2
SUBSTITUTION = 3

class Node():
    def __init__(self, start, target, nodeType=None):
        """ Initialize Node with start and target strings.
        
        Parameters
        ----------
        start: str
        target: str
        nodeType: int, 0-3 which correspond to the constants 
                        ROOT, DELETE, INSERT, and SUBSTITUTION
        """
        self.start = start
        self.target = target
        self.nodeType = nodeType
        self.isLeaf = min(len(self.start), len(self.target)) == 0

        if self.isLeaf:
            self.children = {}
        else:
            self.children = {"delete": Node(start[:-1], target, DELETE),
                            "insert": Node(start, target[:-1], INSERT),
                            "substitution": Node(start[:-1], target[:-1], SUBSTITUTION)}

    def __repr__(self):
        return "<ClassName: Node, Start: '{}', Target: '{}', nodeType: {}>".format(
                                                self.start, self.target, self.nodeType)

    def getChildCost(self, child):
        """ Get the cost of a child, adjusted for the operation that it represents.

        Parameters
        ----------
        child: Node

        Returns
        -------
        cost: int
        path: [Node]
        """
        childCost, childPath = child.getCost()

        costAdjustment = 0

        if child.nodeType in [DELETE, INSERT]:
            costAdjustment = 1

        # Substitution is free if the letters are the same
        elif child.nodeType == SUBSTITUTION:
            if self.start[-1] == self.target[-1]:
                costAdjustment = 0
            else:
                costAdjustment = 1

        return childCost+costAdjustment, childPath


    def getMinChildCostAndPath(self):
        """ Finds minimum cost child and path to that child.
        Returns
        -------
        cost: int
        path: [Node]
        """
        # import pdb; pdb.set_trace()

        # if one string is empty, the cost is the number of inserts required
        # to get to the other one.
        if self.isLeaf:
            cost = max(len(self.start), len(self.target))
            path = [self]

        else:
            allCostPaths = [self.getChildCost(child) for child in self.children.values()]
            cost, childPath = min(allCostPaths, key=lambda x:x[0])
            path = childPath

        return cost, path


    def getCost(self):
        """ Gets the cost and prepends itsself to the path.
        Returns
        -------
        childCost: int
        path: [Node]
        """
        childCost, childPath = self.getMinChildCostAndPath()
        path = [self] + childPath

        return childCost, path



string1 = "kitten"
string2 = "sitting"

string3 = "kit"
string4 = "sitg"


if __name__ == '__main__':
    cost, path =  Node(string2,string1,ROOT).getCost()
    print cost
    for node in path:
        print [node.start, node.target, node.getCost()[0]]

