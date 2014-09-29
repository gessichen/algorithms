# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):

        dummy = ListNode(0)
    	real_previous = dummy 
    	previous = real_previous
    	current = head

    	while current != None:
    		if (previous == dummy or current.val != previous.val) and (current.next == None or current.val != current.next.val):
    			real_previous.next = current
    			real_previous = current
    		previous = current
    		current = current.next

    	real_previous.next = None
    	return dummy.next
    	

l1 = ListNode(1)
l2 = ListNode(2)
l1.next = l2

s = Solution()
ret = s.deleteDuplicates(l1)

while ret != None:
	print ret.val
	ret = ret.next
