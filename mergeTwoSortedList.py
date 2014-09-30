# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        head1 = l1
        head2 = l2 

        dummy = ListNode(0)
        dummy.next = None
        current = dummy

     	while head1 != None and head2 != None:
     		if head1.val < head2.val:
     			current.next = head1
     			current = head1
     			head1 = head1.next
     		else:
     			current.next = head2
     			current = head2
     			head2 = head2.next

     	while head1 != None:
     		current.next = head1
     		current = head1
     		head1 = head1.next

     	while head2 != None:
     		current.next = head2
     		current = head2
     		head2 = head2.next

     	return dummy.next