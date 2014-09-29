# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
    	if head == None:
    		return None

    	dummy = ListNode (0)
    	dummy.next = head
    	cursor = head

       	while cursor != None and cursor.next != None:
#    		print "entered"
    		start = dummy
    		while start != cursor and start.next.val <= cursor.next.val:
    			start = start.next

    		if start == cursor:
    			cursor = cursor.next
    		else:
    			pInsert = cursor.next
    			cursor.next = pInsert.next
    			next = start.next
    			start.next = pInsert
    			pInsert.next = next

#    	print str(head)
    	return dummy.next

s = Solution()

l1 = ListNode(2)
l2 = ListNode(1)
l1.next = l2
l2.next = None

l = s.insertionSortList(l1)

print l.val