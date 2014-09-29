class Solution:
    # @return a tuple, (index1, index2)

    def sumTuples (self, current, target, numbers, tup, findex, sindex):

    	print str(tup)

    	if current == target:
    		return (findex, sindex)

    	elif current > target:
    		findex += 1
    		if numbers[findex] <= target / 2 :
    			return self.sumTuples(numbers[findex] + numbers[findex + 1], target, numbers, (numbers[findex], numbers[findex + 1]), findex, findex + 1)
    		else:
    			return None

    	else:
    		if sindex == len(numbers) - 1:
    			findex += 1
    			if findex > len(numbers) - 2:
    				return None
    			else:
    				return self.sumTuples(numbers[findex] + numbers[findex + 1], target, numbers, (numbers[findex], numbers[findex + 1]), findex, findex + 1)
    		else:
    			return self.sumTuples(numbers[findex] + numbers[sindex + 1], target, numbers, (numbers[findex], numbers[sindex + 1]), findex, sindex + 1)

    def twoSum(self, num, target):
    	num.sort()
    	if len(num) < 2:
    		return None
    	else:
    		return self.sumTuples (0, target, num, (num[0], num[1]), 0, 1)

s = Solution()
tup = s.twoSum ([3,2,4], 6)
print str(tup)