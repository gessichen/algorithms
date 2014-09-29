# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
    	self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers


    def findPath(self, node, lst, sum, target, retlst):
    	if sum + node.val == target:
    		lst.append(node.val)
    		retlst.append(lst)
    	elif sum + node.val > target:
    		return
    	else:
    		lst.append(node.val)
    		print str(lst)
    		if node.left != None:
    			newlst = lst[:]
    			print str(newlst)
    			self.findPath(node.left, newlst, sum + node.val, target, retlst)
    		if node.right != None:
    			newlst = lst[:]
    			self.findPath(node.right, newlst, sum + node.val, target, retlst)



    def pathSum(self, root, sum):
    	if root == None:
    		return None 
    	lst = []
    	retlst = []
    	self.findPath(root, lst, 0, sum, retlst)

    	print str(retlst)
    	return retlst

L = TreeNode(2)
R = TreeNode(2)
T = TreeNode (5)
T.left = L
T.right = R
s = Solution()
s.pathSum(T,7)