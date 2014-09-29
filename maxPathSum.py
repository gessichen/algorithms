# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
   	self.curmax = 0

    def maxPathSum(self, root):
        self.findMax (root)
        return self.curmax

   	def findMax (self, node):
   		if node == None:
   			return 0
   		leftMax = max(self.findMax(node.left), 0)
   		rightMax = max(self.findMax(node.right), 0)
   		premax = leftMax + rightMax + node.val
   			
   		sefl.curmax = max (premax, self.curmax)
   		return node.val + max(leftMax, rightMax)
