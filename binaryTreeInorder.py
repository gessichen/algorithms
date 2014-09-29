# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        if root == None:
        	return []

        stack = [root]
        used = []
        ret = []

        while len(stack) > 0:
        	node = stack.pop()
        	if node in used:
        		ret.append (node.val)
        		continue

        	if node.right != None:
        		stack.append(node.right)
        		
        	stack.append(node)
        	used.append(node)

        	if node.left != None:
        		stack.append(node.left)

        return ret

s = Solution()

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

node1.left = node2
node1.right = node3

ret = s.inorderTraversal(node1)

print ret
