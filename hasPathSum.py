# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean

    def findTarget(self, node, target, current):
    	new = current + node.val
    	if new > target:
    		return False 
    	if new == target and targe.left == None and target.right == None:
    		return True
    	else:
    		return (node.left != None && self.findTarget (node.left, target, new)) or (node.right != None && self.findTarget (node.right, target, new))

    def hasPathSum(self, root, sum):
    	if root == None:
    		return False
        return self.findTarget (root, sum, 0)