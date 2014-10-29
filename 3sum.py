import time

start = time.time()

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    
    def findSum (self, pos, curlst, arr, sum, retlst, index):

    	new = sum + arr[index]

    	if new == 0 and pos == 3:
#    		print 'sum ' +  str(sum) + ' ' + str(arr[index])
    		rightlst = curlst[:]
    		rightlst.append (arr[index])
    		retlst.append (rightlst)
    		return

    	if new <= 0:
    		if pos == 3:
    			return
    		else:
#    			print str (curlst) + ' ' + str(pos)
    			curlst.append (arr[index])
    			for x in xrange (index + 1, len(arr) - 2 + pos):
    				self.findSum(pos + 1, curlst, arr, sum + arr[index], retlst, x)

    			curlst.pop()



    def threeSum(self, num):
    	retlst = []
    	for x in xrange (0, len(num) - 2):
    		self.findSum(1, [], num, 0, retlst, x)
        return retlst


s = Solution()
ret = s.threeSum([-11,-3,-6,12,-15,-13,-7,-3,13,-2,-10,3,12,-12,6,-6,12,9,-2,-12,14,11,-4,11,-8,8,0,-12,4,-5,10,8,7,11,-3,7,5,-3,-11,3,11,-13,14,8,12,5,-12,10,-8,-7,5,-9,-11,-14,9,-12,1,-6,-8,-10,4,9,6,-3,-3,-12,11,9,1,8,-10,-3,2,-11,-10,-1,1,-15,-6,8,-7,6,6,-10,7,0,-7,-7,9,-8,-9,-9,-14,12,-5,-10,-15,-9,-15,-7,6,-10,5,-7,-14,3,8,2,3,9,-12,4,1,9,1,-15,-13,9,-14,11,9])    
print str(time.time() - start)

print ret
