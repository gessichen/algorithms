# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode

    def addWithWeight (self, l1, l2, retl, weight, index):
    	s = (l1.val  + l2.val + weight) % 10
    	w = (l1.val  + l2.val + weight) / 10
    	node = ListNode(s)
    	if index > 0:
    		retl[index - 1].next = node
    	if l1.next == None:
    		node.next = None
    		retl.append(s) 
    		if w > 0:
    			lnode = ListNode(w)
    			node.next = lnode
    			lnode.next = None
    		return retl[0]
    	retl.append(node)
    	l1 = l1.next
    	l2 = l2.next
    	return self.addWithWeight(l1,l2,retl,w,index + 1)

    def addTwoNumbers(self, l1, l2):
    	return self.addWithWeight(l1,l2,[],0,0)


s = Solution()
ret = s.addTwoNumbers ([2,4,3], [5,6,4])
print str(ret.val)