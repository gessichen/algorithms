import time
start_time = time.time()


class Solution:

	def threeSumRec (self, num, index, cnt, cursum, curlst, ret):
		if cursum > 0:
			return
		if cnt == 2:
			if cursum + num[index] == 0:
				curlst.append(num[index])
				newlst = curlst[:]
				ret.append(newlst)
				curlst.pop()

		else:
			cursum = cursum + num[index]
			curlst.append(num[index])
			for i in xrange (index + 1, len(num) + cnt - 1):
				self.threeSumRec (num, i, cnt+1, cursum, curlst, ret)
			curlst.pop()


	def threeSum(self, num):
		if len(num) == 0:
			return []
		ret = []
		num.sort()
		newnum = []

		numDic = {}
		for i in xrange(0, len(num)):
			number = num[i]
			if number in numDic:
				cnt = numDic[number]
				if number == 0:
					if cnt < 3:
						numDic[number] += 1
				else:
					if cnt < 2:
						numDic[number] += 1
			else:
				numDic[number] = 1

		keys = numDic.keys()

		keys.sort()

		for i in xrange(0, len(keys)):
			for j in xrange(0, numDic[keys[i]]):
				newnum.append(keys[i])

#		print newnum

		for i in xrange(0, len(num) - 2):
			self.threeSumRec(num, i, 0, 0, [], ret)

		retDic = {}
		newret = []
		for i in xrange(0, len(ret)):
			lst = ret[i]
			key = ""
			for j in xrange(0, len(lst)):
				key += str(lst[j])
			if key not in retDic:
				newret.append(lst)
				retDic[key] = lst

		return newret

s = Solution()

ret = s.threeSum([-11,-3,-6,12,-15,-13,-7,-3,13,-2,-10,3,12,-12,6,-6,12,9,-2,-12,14,11,-4,11,-8,8,0,-12,4,-5,10,8,7,11,-3,7,5,-3,-11,3,11,-13,14,8,12,5,-12,10,-8,-7,5,-9,-11,-14,9,-12,1,-6,-8,-10,4,9,6,-3,-3,-12,11,9,1,8,-10,-3,2,-11,-10,-1,1,-15,-6,8,-7,6,6,-10,7,0,-7,-7,9,-8,-9,-9,-14,12,-5,-10,-15,-9,-15,-7,6,-10,5,-7,-14,3,8,2,3,9,-12,4,1,9,1,-15,-13,9,-14,11,9])

print str( time.time() - start_time)
print ret