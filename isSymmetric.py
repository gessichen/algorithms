# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean

    def isMirrorSame (self, lNode, rNode):

    	if lNode.val != rNode.val:
    		return False

    	if (lNode.left == None and rNode.right != None) or (lNode.left != None and rNode.right == None):
    		return False

    	if (lNode.right == None and rNode.left != None) or (lNode.right != None and rNode.left == None):
    		return False

    	if lNode.left != None:
    		if self.isMirrorSame (lNode.left,rNode.right) == False:
    			return False

    	if lNode.right != None:
    		if self.isMirrorSame (lNode.right,rNode.left) == False:
    			return False

    	return True


    def isSymmetric(self, root):
     	if root == None:
     		return True
     	if root.left == None and root.right == None:
     		return True
     	if root.left == None and root.right != None:
     		return False
     	if root.left != None and root.right == None:
     		return False
     	return self.isMirrorSame (root.left, root.right)



