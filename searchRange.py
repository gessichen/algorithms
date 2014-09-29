class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]

    def findIndex (self, A, target, left, right):
    	if left > right:
    		return -1
    	middle = (left + right) / 2
    	num = A[middle]
    	print num
    	if num == target:
    		return middle
    	elif target < num:
    		return self.findIndex (A, target, left, middle - 1)
    	else:
    		return self.findIndex (A, target, middle + 1, right)

    def findRightEdge (self, A, target, left, right):
    	if left > right:
    		return -1
    	if left == right:
    		if A[left] == target:
    			return left
    		else:
    			return -1
    	mid = (left + right) / 2
    	if A[mid] == target:
    		right = self.findRightEdge (A, target, mid + 1, right)
    		if right == -1:
    			return mid
    		else:
    			return right
    	else:
    		return self.findRightEdge (A, target, left, mid - 1)

    def findLeftEdge (self, A, target, left, right):
    	if left > right:
    		return -1
    	if left == right:
    		if A[left] == target:
    			return left
    		else:
    			return -1
    	mid = (left + right) / 2
    	if A[mid] == target:
    		left = self.findLeftEdge (A, target, left, mid - 1)
    		if left == -1:
    			return mid
    		else:
    			return left
    	else:
    		return self.findLeftEdge (A, target, mid + 1, right)


    def searchRange(self, A, target):
        if len (A) < 1 :
        	return [-1,-1]
        index = self.findIndex (A, target, 0, len(A) - 1)
        if index == -1:
        	return [-1,-1]

        print index
        left = self.findLeftEdge (A, target, 0, index - 1)
        right = self.findRightEdge(A, target, index + 1, len(A) - 1)

        if left == -1 and right == -1:
        	return [index,index]
        if left == -1:
      		return [index, right]
      	if right == -1:
      		return [left, index]
      	return [left, right]



s = Solution()
s.searchRange([1], 1)

