# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumTrees (self, node, totalsum, lst):
    	if node.left == None and node.right == None:
    		pathsum = node.val
    		l = len(lst)
    		for i in xrange (l-1,-1,-1):
    			pathsum += pow(10, l-i) * lst[i]
    		totalsum += pathsum

    	else:
    		lst.append (node.val)
    		if node.left != None:
    			totalsum = self.sumTrees (node.left, totalsum, lst)
    		if node.right != None:
    			totalsum = self.sumTrees (node.right, totalsum, lst)

    		lst.pop()
    	return totalsum

    def sumNumbers(self, root):
    	if root == None:
    		return 0
        return self.sumTrees(root, 0, [])
t1 = TreeNode(1)
#t2 = TreeNode(2)
#t3 = TreeNode(3)
t4 = TreeNode(4)
#t1.left = t2
t1.right = t4
#t2.left = t4



s = Solution()
ret = s.sumNumbers(t1)
print ret