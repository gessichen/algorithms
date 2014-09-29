# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
    	previous = None
    	current = head

    	cnt = 1
    	begin_previous = None

    	while cnt <= n:
    		if cnt == m:
#    			print current.val
    			begin = current
    			begin_previous = previous
    			previous = current
    			current = current.next

    		elif cnt > m:
    			tmp = current.next
    			current.next = previous
    			previous = current
    			current = tmp

    		else:
    			previous = current
    			current = current.next
    		cnt += 1

    	if begin_previous != None:
    		begin_previous.next = previous
    	begin.next = current 

    	if begin_previous == None:
    		return previous
    	else:
    		return head


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = None


s = Solution()
h = s.reverseBetween(l1,1,1)

cur = h 
while cur != None:	
	print cur.val
	cur = cur.next



