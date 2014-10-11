# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @return a list of tree node

    def generateTreesWithList(self, lst):
    	if len(lst) == 0:
    		return None

    	if len(lst) == 1:
    		return [TreeNode(lst[0])]

    	trees = []
    	for i in xrange(0, len(lst)):
    		leftlst = self.generateTreesWithList(lst[0:i])
    		rightlst = self.generateTreesWithList(lst[i+1,len(lst)])
    		if leftlst == None and rightlst!= None:
    			for j in xrange (0, len(rightlst)):
    				root = TreeNode(lst[i])
    				root.right = rightlst[j]
    				trees.append(root)

    		else if right == None and leftlst!=None:
    			for j in xrange (0, len(leftlst)):
    				root = TreeNode(lst[i])
    				root.left = leftlst[j]
    				trees.append(root)

    		else:
    			for j in xrange(0, len(leftlst)):
    				for k in xrange(0, len(rightlst)):
    					root = TreeNode(lst[i)
    					root.left = leftlst[j]
    					root.right = rightlst[k]
    					trees.append(root)


    	return trees

    def generateTrees(self, n):
    	nums = []
    	for i in xrange (1,n+1):
    		nums.append(i)
    	return self.generateTreesWithList(nums)

