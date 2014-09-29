# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
    	smallerBeg = ListNode(0)
    	smallerEnd = smallerBeg
    	biggerBeg = ListNode(0)
    	biggerEnd = biggerBeg

    	pointer = head

    	while pointer != None:
    		if pointer.val < x:
    			smallerEnd.next = pointer
    			smallerEnd = pointer

    		else:
    			biggerEnd.next = pointer
    			biggerEnd = pointer

    		pointer = pointer.next


    	smallerEnd.next = biggerBeg.next
    	biggerEnd.next = None

    	return smallerBeg.next
        