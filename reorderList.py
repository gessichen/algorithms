# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
    	if head == None:
    		return None
    	if head.next == None:
    		return head

       	cursor = head
       	lstlen = 0
       	while cursor != None:
       		cursor = cursor.next
       		lstlen += 1

       	halfP = head
       	cnt = 0
       	while cnt < lstlen / 2:
       		halfP = halfP.next
       		cnt += 1
       	
       	#now head is head, halfP is the pointer of the middle pointer
       	cursor = halfP
       	pre = None
       	while cursor != None:
       		pnext = cursor.next
       		cursor.next = pre 
       		pre = cursor
       		cursor = pnext

       	i = 0
       	dummy = ListNode(0)
       	dummy.next = None
       	cursor = dummy
       	while i < lstlen / 2:

       		print head.val
       		print pre.val

       		cursor.next = head
       		cursor = head
       		head = head.next
       		cursor.next = pre 
       		cursor = pre
       		pre = pre.next
       		cursor.next = None

       		i += 1

       	if lstlen % 2 == 1:
       		cursor.next = pre
       		cursor = cursor.next
       		cursor.next = None
       
       	return dummy.next


s = Solution()
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

ret = s.reorderList(l1)

print str(ret)

while ret != None:
	print ret.val
	ret = ret.next






