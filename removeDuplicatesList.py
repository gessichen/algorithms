# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        previous = None
        current = head

        while current != None:
        	if previous == None:
        		previous = current
        		current = current.next

        	else:
        		if previous.val == current.val:
        			previous.next = current.next
        			current = current.next

        		else:
        			previous = current
        			current = current.next


     	return head 

        		