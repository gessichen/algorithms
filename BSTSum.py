# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.leftNodesNum = 0
        self.rightNodesNum = 0
        self.level = 0
        self.levelSum = 0
        self.leftsum = 0
        self.rightsum = 0

# time:O(N * logN) space:O(N)
def insertNode (val, tree, level):
	if tree == None:
		tree = TreeNode(val)
		tree.level = level
		return tree
	else:
		if val < tree.val:
			tree.left = insertNode (val, tree.left, level + 1)
			tree.leftNodesNum += 1
		else:
			tree.right = insertNode (val, tree.right, level + 1)
			tree.rightNodesNum += 1
		return tree

def printTree (tree):
	if tree == None:
		print "None"
	else:
		print str(tree.val) + ' ' + str(tree.levelSum) + ' ' + str(tree.sum)
		printTree(tree.left)
		printTree(tree.right)	

# time:O(N)
def levelSum (tree):
	if tree.left != None:
		tree.leftsum = 0
		tree.leftsum += levelSum(tree.left) + 1 + tree.left.leftNodesNum + tree.left.rightNodesNum
	if tree.right != None:
		tree.rightsum = 0
		tree.rightsum += levelSum (tree.right) + 1 + tree.right.leftNodesNum + tree.right.rightNodesNum
	tree.sum = tree.leftsum + tree.rightsum
	return tree.leftsum + tree.rightsum


def sumAlg(tree, rightNodesLst):
	if tree == None:
		return
	else:
		for i in xrange (0, len(rightNodesLst)):
			nodesTuple = rightNodesLst[i]
			tree.sum += ((tree.level - nodesTuple[0]) * nodesTuple[1] + nodesTuple[2])
		sumAlg(tree.right,rightNodesLst)
		t = (tree.level, tree.rightNodesNum, tree.rightsum)
		rightNodesLst.append (t)
		sumAlg(tree.left, rightNodesLst)
		rightNodesLst.remove (t)

def allSum(tree):
	if tree == None:
		return 0
	return allSum(tree.left) + allSum(tree.right) + tree.sum

def buildTree (lst):
	tree = None
	for i in xrange (0, len(lst)):
		tree = insertNode (lst[i],tree, 0)
		levelSum(tree)
		sumAlg(tree,[])
		s = allSum (tree)
		print s
#	printTree(tree)
	return tree

num = int(raw_input())
numstr = (raw_input()).split()
lst = []
for i in xrange(0, len(numstr)):
	lst.append (int(numstr[i]))


tree = buildTree(lst)

levelSum(tree)
sumAlg(tree,[])
s = allSum (tree)
print s

#printTree(tree)


