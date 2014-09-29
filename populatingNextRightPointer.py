# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
    	if root == None:
    		return

    	nodeStack = [root]

    	while len(nodeStack) > 0:

    		for i in xrange (0, len(nodeStack) - 1):
    			nodeStack[i].next = nodeStack[i+1]
    		nodeStack[len(nodeStack) - 1].next = None

    		l = len(nodeStack)
    		for i in xrange (0, l):
    			node = nodeStack.pop(0)
    			if node.left != None:
    				nodeStack.append(node.left)
    			if node.right != None:
    				nodeStack.append(node.right)


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

node1.left = node2
node1.right = node3

s = Solution()

s.connect(node1)