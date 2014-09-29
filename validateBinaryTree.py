# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def validBST(self, node, minVal, maxVal):
    	if node == None:
    		return True
    	if node.val <= minVal or node.val >= maxVal:
    		return False

    	ret = self.validBST(node.left, minVal, node.val) and self.validBST(node.right,node.val,maxVal)

    	return ret

    def isValidBST(self, root):
    	return self.validBST(root, float("-inf"), float("inf"))



node1 = TreeNode(10)
node2 = TreeNode(5)
node3 = TreeNode(15)
node4 = TreeNode(6)
node5 = TreeNode(20)
node1.left = node2
node1.right = node3

node3.left = node4
node4.right = node5

s = Solution()
ret = s.isValidBST(node1)

print ret


