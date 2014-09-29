# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        if root == None:
        	return []

        result = []
        stack = [root.val]

        while len(stack) > 0:
        	l = len(stack)
        	stackcpy = []
        	for i in xrange (0, l):
        		node = stack.pop()
        		stackcpy.append(node.val)
        		if node.left != None:
        			stack.append(node.left)
        		if node.right != None:
        			stack.append(node.right)
        	result.append(stackcpy)

       	result.reverse()
       	return result


s = Solution()
node1 = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)

node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5

ret = s.levelOrderBottom(node1)

print len(ret)
