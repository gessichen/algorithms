# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode

    def mergeSortedList (self, h1, size1, h2, size2):
   		tmpHead = ListNode(0)
   		cursor = tmpHead
   		c1 = 0
   		c2 = 0
   		while c1 < size1 and c2 < size2:
   			if h1.val < h2.val:
   				cursor.next = h1
   				cursor = h1
   				h1 = h1.next
   				c1 += 1
   			else:
   				cursor.next = h2 
   				cursor = h2
   				h2 = h2.next
   				c2 += 1
   			

   		while c1 < size1:
   			cursor.next = h1
   			cursor = h1
   			h1 = h1.next
   			c1 += 1

   		while c2 < size2:
   			cursor.next = h2
   			cursor = h2
   			h2 = h2.next
   			c2 += 1

   		cursor.next = None
   		return tmpHead.next

    def sorting (self, head, size):
   		if size == 1:
   			return head
   		h1 = head
   		h2 = head
   		for i in xrange(0, size / 2):
   			h2 = h2.next

   		list1 = self.sorting (h1, size / 2)
   		list2 = self.sorting (h2, size - size / 2)

   		return self.mergeSortedList (list1, size/2, list2, size - size/2)

    def sortList(self, head):
        if head == None:
        	return None

        lstcnt = 0
        plist = head
        while  plist != None:
       		lstcnt += 1
       		plist = plist.next

      	return self.sorting (head, lstcnt)

   	

   	


