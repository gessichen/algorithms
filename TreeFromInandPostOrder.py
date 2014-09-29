# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
    	if len(postorder) == 0:
    		return None

    	if len(postorder) == 0:
    		return TreeNode(postorder[0])

    	l = len(postorder)
    	root = TreeNode(postorder[l-1])

    	index = inorder.index(postorder[l-1])
    	root.left = self.buildTree(inorder[0:index], postorder[0:index])
    	root.right = self.buildTree(inorder[index+1:l], postorder[index,l-1])

    	return root


def printTree (tree):
	if tree == None:
		print "#"
		return
	print tree.val
	printTree(tree.left)
	printTree(tree.right)

