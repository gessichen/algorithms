class Solution:
    # @param s, a string
    # @return a list of strings

    def restoreRec(self, s, current, index, strindex, lst):
    	l = len(s) - strindex
    	if l < 4 - index:
    		return
    	if l > (4 - index) * 3:
    		return

    	if index == 3:
#    		print "reach final"
    		num_str = s[strindex:]
    		num = int(num_str)
#    		print num
    		if l >= 2 and num < pow(10,l-1):
    			return

    		if num <= 255:
    			newip = ""
    			for i in xrange (0, len(current)):
    				newip += current[i]
    				newip += "."
    			newip += num_str
    			lst.append(newip)
    	else:
    		limit = l
    		if l > 3:
    			limit = 3
    		for i in xrange(1, limit+1):
    			addr = s[strindex:strindex + i]
    			addr_int = int(addr)
#    			print addr_int
    			if addr_int <= 255:
#    				print "yes"
    				if i >= 2 and addr_int < pow(10,i-1):
    					print addr_int
    					return
    				current.append(addr)
    				self.restoreRec(s, current, index+1, strindex + i, lst)
    				current.pop()

    def restoreIpAddresses(self, s):
    	ret = []
    	self.restoreRec(s, [], 0, 0, ret)
    	return ret


print pow(10,2)

s = Solution()
ret = s.restoreIpAddresses("255255255255")

print ret