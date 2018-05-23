class treeNode:
    def __init__(self, nameValue, numOccur, parentNode):
        self.name = nameValue
        self.count = numOccur
        self.nodeLink = None
        self.parent = parentNode
        self.children = {}
    
    def inc(self, numOccur):
        self.count += numOccur
    
    def disp(self, ind=1):
        print '  '*ind, self.name, ' ', self.count
        for child in self.children.values():
            child.disp(ind+1)

def updateHeader(nodeToTest, targetNode):
    while nodeToTest.nodeLink != None:
        nodeToTest = nodeToTest.nodeLink
    nodeToTest.nodeLink = targetNode

header = treeNode("None", 0, None)
header.disp()

node1 = treeNode("one", 1, None)
updateHeader(header, node1)
header.nodeLink.disp()

node2 = treeNode("two", 1, None)
updateHeader(header, node2)
header.nodeLink.nodeLink.disp()
