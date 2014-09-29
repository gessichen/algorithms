# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
       	self.val = x
        self.left = None
	   	self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing

    def connectQueue(self, queue):
    	qlen = len(queue)
    	cnt = 0
    	while cnt < qlen:
    		node = queue[cnt]
    		if node.left != None:
    			queue.append(node.left)
    		if node.right != None:
    			queue.append(node.right)
    		if cnt == qlen - 1:
    			node.next = None
    		else:
    			node.next = queue[cnt + 1]
    		queue.pop(0)
    		cnt += 1
    	self.connectQueue(queue)


    def connect(self, root):
    	if root == None:
    		return None
       	q = []
       	q.append(root)
       	self.connectQueue(q)
       	return root
