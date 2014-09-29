# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
    	if root == None:
    		return None

        nodeStack = [root]
       	ret = []

       	while len(nodeStack) > 0:
       		node = nodeStack.pop()
       		ret.append(node.val)

       		if node.left != None:
       			nodeStack.append(node.left)

       		if node.right != None:
       			nodeStack.append(node.right)

       	ret.reverse()
       	return ret



s = Solution()

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

node1.right = node2
node2.left = node3

ret = s.postorderTraversal(node1)

print ret