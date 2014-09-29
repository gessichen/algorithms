# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer

    def onSameLine (self,p1,p2,p3):
    	diff13Y = (p3.y - p1.y) * 1.0
    	diff13X = (p3.x - p1.x) * 1.0
    	v13 = diff13Y / diff13X

    	diff12Y = (p2.y - p1.y) * 1.0
    	diff12X = (p2.x - p1.x) * 1.0
    	v12 = diff12Y / diff12X

#    	print str(v13) + " " + str(v12)
    	return v13 == v12


    def maxPoints(self, points):
    	if points == None:
        	return 0
    	xDic = {}
    	ppDic = {}

    	for i in xrange (0, len(points)):
    		p = points[i]
    		if xDic.has_key (p.x):
    			xDic[p.x] += 1
    		else:
    			xDic[p.x] = 1

    		allkeys = ppDic.keys()
#    		print str(ppDic)

#			the 1st point has no other point to make the line pair
    		if (len(allkeys) == 0):
    			firstKey = (p,None)
    			ppDic[firstKey] = [p]
    		else:
    			for j in xrange(0, len(allkeys)):
    				ptuple = allkeys[j]
    				p1 = ptuple[0]
    				lst = ppDic[ptuple]
    				# if these two points are not in the same vertical line
    				if p1.x != p.x:
    					p2 = ptuple[1]
    					if p2 == None:
    						ppDic.pop(ptuple, None)
    						newtuple = (p1,p)
    						ppDic[newtuple] = [p1,p]
    					else:
    						if self.onSameLine (p1,p2,p):
    							lst.append(p) 
    						else:
    							for k in xrange (0, len(lst)):
    								oldp = lst[k]
    								newtuple = (oldp, p)
    								if oldp.x != p.x:
    									ppDic[newtuple] = [oldp, p]

    	maxCnt = 0

    	allxkeys = xDic.keys()
    	for i in xrange (0, len(allxkeys)):
    		xkey = allxkeys[i]
    		cnt = xDic[xkey]
    		if cnt > maxCnt:
    			maxCnt = cnt

    	alltuplekeys = ppDic.keys()
    	for i in xrange (0, len(alltuplekeys)):
    		tuplekey = alltuplekeys[i]
    		cnt = len(ppDic[tuplekey])
    		if cnt > maxCnt:
    			maxCnt = cnt

    	return maxCnt

p1 = Point(0,0)
p2 = Point(1,1)
p3 = Point(1,-1)
p4 = Point(2,2)
p5 = Point(7,8)

s = Solution()
ret = s.maxPoints ([p1,p2,p3,p4,p5])
print ret


