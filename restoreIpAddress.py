class Solution:
    # @param s, a string
    # @return a list of strings


    def convert2IP(self, ipaddr):
    	ret = ""
    	for i in xrange (0, len(ipaddr)-1):
            ret += ipaddr[i]

            ret += '.'
        ret += ipaddr[len(ipaddr) - 1]
        return ret

    def getAddress (self, ret, s, index, num, ipaddr):
        print str(ipaddr)
        print index
    	if len(ipaddr) == 4:
    		if index == len(s):
    			newip = self.convert2IP(ipaddr)
    			ret.append(newip)
            return

    	if index + num > len(s):
    		return
    	substr = s[index:index + num]
    	ipnum = int(substr)
    	if ipnum > 255:
    		return
    	ipaddr.append (substr)
    	for i in xrange (1,4):
    		self.getAddress(ret,s,index + num,i,ipaddr)
    	ipaddr.pop()


    def restoreIpAddresses(self, s):
        ret = []
        for i in xrange (1,4):
    		self.getAddress(ret,s,0,i,[])
        return ret


s = Solution()

ret = s.restoreIpAddresses("25525511135")

print str(ret)