class Solution:
    # @return an integer
    def reverse(self, x):
        if x < 0:
        	return (-1) * self.reverse(-x)

        ret = 0
        while  x > 0:
       		ret = ret * 10 + x % 10
       		x = x // 10

       	return ret


s = Solution()
ret = s.reverse(132)

print ret