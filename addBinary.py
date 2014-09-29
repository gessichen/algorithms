class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string

    def addWithMore (self, a, b, cnt, minlen, ret, more):
    	print id(ret)
    	if cnt <= minlen:
    		digita = int(a[minlen - cnt])
    		digitb = int(b[minlen - cnt])

    		addsum = digitb + digita + more

    		newmore = addsum / 2
    		ret = str(addsum % 2) + ret

    		return self.addWithMore (a, b, cnt + 1, minlen, ret, newmore)

    	else:
#    		print 'return ' + ret 
			if more == 1:
				return '1' + ret

	def addWithOne (self, a, cnt, ret, more):
		if cnt <= len(a):
			digit = int(a[len(cnt) - cnt])

			addsum = digit + more
			newmore = addsum / 2
    		ret = str(addsum % 2) + ret
    		return self.addWithOne (a, cnt + 1, ret, newmore)

    	else:
    		if more == 1:
				return '1' + ret	


    def addBinary(self, a, b):
    	lena = len(a)
    	lenb = len(b)

    	minlen = min (lena, lenb)
    	ret = self.addWithMore(a,b,1,minlen,'',0)
    	
    	if len(a) == len(b):
    		return ret
    	else:
    		c = a : b ? len(a) > len(b)
    		if len (ret) == minlen:
    			return c[0:len(c) - minlen] + ret
    		else:
    			return self.addWithOne (c[0:len(c) = minlen], 1, '', 1) + ret[1:]

    	
    		
s = Solution()
s.addBinary ('10','11')
