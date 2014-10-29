def canCutRec (dic, N):
	if N <= 0:
		return False

	for key in dic.keys():
		if dic[key] > 0:
			remain = N - key
			dic[key] = dic[key] - 1
			if remain in dic and dic[remain] > 0:
				return True
			if canCutRec(dic, N - key):
				return True
			else:
				dic[key] = dic[key] + 1

	return False

def canCut (ropes,N):
	ropeDic = {}
	for i in xrange (0, len(ropes)):
		r = ropes[i]
		if r in ropeDic:
			ropeDic[r] = ropeDic[r] + 1
		else:
			ropeDic[r] = 1

	return canCutRec(ropeDic, N)

ropes = [12,73,4,5,1]

ret = canCut(ropes, 10)

print ret 