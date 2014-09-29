# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        self.node1 = None
        self.node2 = None
        self.pre = None

    	self.inorderRec(root)
    	tmp = node1.val
    	self.node1.val = node2.val
    	self.node2.val = tmp
    	return root

    def inorderRec (self, root):
    	if root == None:
    		return 

    	self.inorderRec(root.left)

    	if pre == None:
    		self.pre = root

    	if self.node1 == None and self.pre.val > self.root.val:
    		self.node1 = self.pre
    		self.node2 = root 

    	elif pre.val > root.val:
    		self.node2 = root 

    	self.pre = root
    	self.inorderRec(root.right)

