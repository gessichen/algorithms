class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if s == None or len (s) == 0:
        	return True

        l = len(s)

        news = ""
      	for i in xrange (0,l):
      		c = s[i]
      		if (c >= 'a' and c <= 'z') or (c >= "A" and c <= "Z")  or (c >= "0" and c <= "9"):
      			news += c
#      	print news
      	ll = len(news)
      	if ll <= 1:
      		return True

     	i = 0
     	j = ll - 1

     	while i < j:
     		start = news[i]
     		end = news[j]

     		if start.lower() != end.lower():
#     			print start
#     			print end
     			return False

     		i += 1
     		j -= 1

     	return True

s = Solution()

ret = s.isPalindrome("1a1")

print ret