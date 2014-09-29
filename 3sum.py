class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    
    def findSum (self, pos, curlst, arr, sum, retlst, index):

    	print str(curlst) + ' ' + str (arr[index])

    	new = sum + arr[index]

    	if new == 0 and pos == 3:
    		print 'sum ' +  str(sum) + ' ' + str(arr[index])
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
    	print str(retlst)



s = Solution()
s.threeSum([-4,-1,-1,0,1,2])        