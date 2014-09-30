class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
    	if len(s1) + len(s2) != len(s3):
    		return False
    	for i in xrange (0, len(s1)+1):
    		row = []
    		for j in xrange (0, len(s2)+1):
    			if i == 0 and j == 0:
    				row.append(True)
    			else:
	    			tmp = False
	    			if j > 0:
	    				tmp = tmp or (row.append(row[j-1] and s2[j-1] == s3[i+j-1]))
	    			if i > 0:
	    				tmp = tmp or (prev_row[j] and s1[i-1] == s3[i+j-1])

    				row.append(tmp)
    		prev_row = row


    	return row[len(s2)]




