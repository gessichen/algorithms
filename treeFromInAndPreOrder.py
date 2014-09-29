# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if len(inorder) == 0:
        	return None

        if len(inorder) == 1:
        	return TreeNode(inorder[0])

        l = len(inorder)

       	root = TreeNode(preorder[0])
       	index = preorder.index(preorder[0])

       	root.left = self.buildTree (preorder[1:index + 1], inorder[0:index])
       	root.right = self.buildTree(preorder[index+1:l], inorder[index+1,l])

       	return root