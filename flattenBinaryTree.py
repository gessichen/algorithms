# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place

    def flatten(self, root):
        if root == None:
        	return None

        cursor = root
        stack = []

        while True:
       		if cursor.right != None:
       			stack.append(cursor.right)
       		if cursor.left != None:
       			cursor.right =cursor.left
       			cursor.left = None
       			cursor = cursor.right
       		else:
       			if len(stack) == 0:
       				return root
       			node = stack.pop()
       			cursor.right = node
       			cursor.left = None
       			cursor = cursor.right




node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node1.left = node2
node1.right = node5

node2.left = node3
node2.right = node4

s = Solution()
ret = s.flatten(node1)

while ret!= None:
	print ret.val
	ret = ret.right






