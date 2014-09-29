# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode

    def copyWithDic (self, head, dic):
    	if head == None:
    		return None

    	if head in dic:
    		return dic[head]

    	node = RandomListNode(head.label)
    	dic[head] = node
    	node.next = self.copyWithDic(head.next, dic)
    	node.random = self.copyWithDic(head.random,dic)


    def copyRandomList(self, head):
        return self.copyWithDic(head, {})