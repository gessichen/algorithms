class Solution:
    # @param num, a list of integer
    # @return a list of integer

    def swapLst (self, num):
    	l = len(num)
    	for i in xrange(0, l / 2):
    		tmp = num[i]
    		num[i] = num[l-1-i]
    		num[l-1-i] = tmp
#    	print str(num)

    def nextPermutation(self, num):
    	l = len(num)
    	swapped = False
    	for i in xrange (l - 1, 0 ,-1):
    		curr_digit = num[i]
    		prev_digit = num[i - 1]
    		if prev_digit < curr_digit:
    	#		print 'entered'
    			found = False
    			for j in xrange (i, l - 1):
	    			if num[j] > prev_digit and num[j + 1] <= prev_digit:
	    				found = True
	    				num[i - 1] = num[j]
	    				num[j] = prev_digit
	    				
	    				for k in xrange (0, (l - i) / 2):
	    					tmp = num[i + k]
	    					num[i + k] = num[l - k - 1]
	    					num[l - k -1] = tmp
	    				break
	    		if found == False:
	    			num[i - 1] = num[l - 1]
	    			num[l - 1] = prev_digit
	    			for k in xrange (0, (l - i) / 2):
	    				tmp = num[i + k]
	    				num[i + k] = num[l - k - 1]
	    				num[l - k -1] = tmp
	    		swapped = True	
	    		break
    	if swapped == False:
    		self.swapLst (num)
    	return num 

s = Solution()
ret = s.nextPermutation ([6,9,5,3])
print str(ret)