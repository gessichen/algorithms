# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node

    def buildTree(self, head, length):
#    	print head.val
    	if length == 0:
    		return None
    	if length == 1:
    		return TreeNode(head.val)

    	cursor = head
    	for i in xrange(0, length / 2):
    		cursor = cursor.next
#    		print cursor.val

    	root = TreeNode(cursor.val)

    	root.left = self.buildTree(head, length/2)
    	root.right = self.buildTree(cursor.next, length - length/2 - 1)

    	return root

    def sortedListToBST(self, head):
    	if head == None:
    		return None

    	length = 0
    	p = head
    	while p != None:
    		length += 1
    		p = p.next
    	return self.buildTree (head, length)

def printTree (tree):
	if tree == None:
		print "#"
		return
	print tree.val
	printTree(tree.left)
	printTree(tree.right)

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = None 

s = Solution()

tree = s.sortedListToBST(l1)

printTree(tree)











