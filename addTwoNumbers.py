# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
   		dummy = ListNode(0)
   		current = dummy
   		levelUp = 0
   		while l1 != None or l2 != None:
   			newVal = levelUp
   			if l1 != None:
   				newVal += l1.val
   				l1 = l1.next
   			if l2 != None:
   				newVal += l2.val
   				l2 = l2.next

   			if newVal >= 10:
   				levelUp = 1
   				newVal -= 10
   			else:
   				levelUp = 0
   			newNode = ListNode(newVal)
   			current.next = newNode
   			current = newNode

   		if levelUp == 1:
   			current.next = ListNode(1)

   		return dummy.next


s = Solution()

l1 = ListNode(2)
l2 = ListNode(4)
l3 = ListNode(3)

l1.next = l2
l2.next = l3


l4 = ListNode(5)
l5 = ListNode(6)
l6 = ListNode(4)

l4.next = l5
#l5.next = l6

ret = s.addTwoNumbers(l1,l4)

while ret != None:
	print ret.val
	ret = ret.next





