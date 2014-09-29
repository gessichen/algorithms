# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer

    def findMin(self, node):
    	if node.left == None and node.right == None:
    		return 1
    	elif node.left == None and node.right != None:
    		return 1 + self.findMin(node.right)
    	elif node.left != None and node.right == None:
    		return 1 + self.findMin(node.left)
    	else:
    		return min (self.findMin(node.left), self.findMin(node.right)) + 1

    def minDepth(self, root):
    	if root == None:
    		return 0
    	return findMin(root)
