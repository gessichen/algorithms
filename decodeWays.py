class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
   		if len(s) == 0 or s[0] =="0":
   			return 0 

   		curWays = 1
   		preWays = 0
   		zerocnt = 0
   		prec = ''

   		i = 0
   		while i < len(s):
   			c = s[i]
   			if int(c) == 0:
   				zerocnt += 1
   				if zerocnt > 1:
   					return 0
   			else:
   				zerocnt = 0


   			pair = prec + c
#   			print pair
   			value = int(pair)

   			if value % 10 == 0 
   				if value > 20:
   					return 0 
   				else:
   					curWays = preWays

   			elif value <= 26 and value > 10:
   				tmp = curWays
   				curWays = curWays + preWays
   				preWays = tmp
   			
   			else:
   				preWays = curWays
   			
   			prec = c
   			i+=1

   		return curWays

s = Solution()
ret = s.numDecodings("10")
print ret