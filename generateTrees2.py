# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @return a list of tree node

    def serializeTree (self, TreeNode):
    	

    def generateNodeWithList(self, lst):
    	l = len(lst)
    	if l == 0:
    		return None
    	treelst = []
    	for i in xrange (0,l):
    		leftlst = self.generateNodeWithList (lst[0:i])
    		rightlst = self.generateNodeWithList  (lst[i + 1:l])
    		if leftlst == None:
    			if rightlst == None:
    				treelst.append ( TreeNode (lst[i]) )
    			else:
	    			for j in xrange (0, len(rightlst)):
	    				node = TreeNode (lst[i])
	    			 	node.right = rightlst[j]
	    			 	treelst.append (node)
    		else:
    			if rightlst == None:
    				for j in xrange (0, len(leftlst)):
	    				node = TreeNode (lst[i])
	    			 	node.left = leftlst[j]
	    			 	treelst.append (node)
    			else:
    			 	for j in xrange (0, len(leftlst)):
    			 		for k in xrange (0, len(rightlst)):
    			 			node = TreeNode (lst[i])
    			 			node.left = leftlst[j]
	    			 		node.right = rightlst[k]
	    			 		treelst.append (node)
	   	return treelst

    def generateTrees(self, n):
    	lst = []
    	for i in xrange (0, n):
    		lst.append(i)
        treelst = self.generateNodeWithList(lst)
        print str(len(treelst))

s = Solution()
s.generateTrees(3)
