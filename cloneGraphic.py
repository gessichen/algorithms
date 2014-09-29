# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node

    def cloneWithDic(self, node, dic):

    	if node in dic:
    		return dic[node]

    	newnode = UndirectedGraphNode(node.label)
    	dic[node] = newnode

    	for i in xrange (0, len(node.neighbors)):
    		neighbor = node.neighbors[i]
    		newnode.append (self.cloneWithDic(neighbor, dic))

    	return newnode


    def cloneGraph(self, node):
        if node == None:
        	return None

        return self.cloneWithDic(node)
