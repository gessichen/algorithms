# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode

    def swapParisRec(self, head, current):
   		if current == None or current.next == None:
   			head.next = current

   		else:

   			newCurrent = current.next.next

   			head.next = current.next
   			head.next.next = current

   			head = newCurrent

   			self.swapParisRec(current,newCurrent)


    def swapPairs(self, head):
    	dummyHead = ListNode(0)
    	self.swapParisRec(dummyHead,head)
    	return dummyHead.next 

s = Solution()
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)

l1.next = l2
l2.next = l3
l3.next = l4

ret = s.swapPairs(l1)

while ret != None:
	print ret.val
	ret = ret.next

        