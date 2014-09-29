# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):

    	slowPointer = head
    	fastPointer = head

    	while fastPointer != None and fastPointer.next != None:
    		slowPointer = slowPointer.next
    		fastPointer = fastPointer.next.next

    		if (slowPointer == fastPointer):
    			return True

    	return False

l1 = ListNode(0)
l2 = ListNode(1)
l3 = ListNode(2)

l1.next = l2
l2.next = l3
l3.next = None

s = Solution()
ret = s.hasCycle(l1)

if ret == True:
	print "True"
else:
	print "False"



