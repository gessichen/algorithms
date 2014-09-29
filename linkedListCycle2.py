# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        slowPointer = head
        fastPointer = head

        while fastPointer != None and fastPointer.next != None:
        	slowPointer = slowPointer.next
        	fastPointer = fastPointer.next.next

        	if fastPointer == slowPointer:
        		cnt = 1
        		p = fastPointer.next
        		while p != slowPointer:
        			p = p.next
        			cnt += 1       		

        		fastPointer = head 
        		for i in xrange (0, cnt):
        			fastPointer = fastPointer.next

        		slowPointer = head
        		while slowPointer != fastPointer:
        			slowPointer = slowPointer.next
        			fastPointer = fastPointer.next

        		return fastPointer
        		
        return None

l1 = ListNode(0)
l2 = ListNode(1)
l3 = ListNode(2)

l1.next = l2
l2.next = l3
l3.next = l1

s = Solution()
ret = s.detectCycle(l1)

if ret == None:
	print "no cycle"
else:
	print ret.val

