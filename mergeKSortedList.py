# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        k = len(lists)

       	noneCnt = 0

       	dummyHead = ListNode(0)
       	head = dummyHead

       	while noneCnt != k:
       		noneCnt = 0
       		index = -1
       		minVal = float("inf")
       		for i in xrange (0, k):
       			lst = lists[i]
       			if lst == None:
       				noneCnt += 1
       				continue
       			else:
       				if lst.val < minVal:
       					minVal = lst.val
       					index = i

       		if noneCnt != k:
       			minlst = lists[index]
       			head.next = minlst
       			head = head.next
       			minlst = minlst.next


       	return dummyHead.next