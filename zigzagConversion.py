class Solution:
    # @return a string

    def convertRec(self,direction, row, nSpace, index, s, l, nRows, strlsts):
    	if index == l:
    		return
    	for i in xrange(0, nSpace):
    		strlsts[row].append(" ")
    	strlsts[row].append(s[index])
    	if row == nRows - 1:
    		direction = -1
    		self.convertRec(direction, row-1, 0, index+1, s, l, nRows, strlsts)
    	elif row == 0:
    		direction = 1
    		self.convertRec(direction, row+1, 0, index+1, s, l, nRows, strlsts)

    	else:
    		self.convertRec(direction, row+direction, nSpace+1, index+1, s, l, nRows, strlsts)

    
    def convert(self, s, nRows):

    	if nRows == 1:
    		return s

    	strlsts = []
    	for i in xrange (0, nRows):
    		strlsts.append([])

    	self.convertRec(1, 0, 0, 0, s, len(s), nRows, strlsts)

#    	print strlsts

    	ret = ""
    	for i in xrange(0, len(strlsts)):
    		for j in xrange(0, len(strlsts[i])):
    			if strlsts[i][j] != " ":
    				ret += strlsts[i][j]
    	return ret

s = Solution()
ret = s.convert("yjvsbxetkierlqfbxyetjbyqqgrtrurpfmkhjocwyjpjzunxsrqdurtkxngqjxgokqxvgarejgqkadhuuayortbqgjhpgpgsfdolffrqmhbokklgklxdeywnhfepukibqwoxbfqpnrgzdrgocdtidpxmucbqojrghfelnuaangzszhibmcmptjbqnfgcoykyfojskluzuwstdaxqejhyuloiqumguwecnnuzbpzvntoqvliawsatdobtkpzhlejytfauwzrjugcptmrserlhhoaudcboimpdrpaqqrzmxddtqvluoweymgspitfshwwynwqfnqrnvvilstiirmgduyuftzxawvbjrrphjiwffgszzcisqoxlprqkqnloloaehrltzjahpsgqxoknfhywyogrethphhtrahkcsmjkgpcdgnrnwpjxgpqkjxbshwlhfxjyjskqkmtqbkdycovidnuokvjrtubzukzdfjtpxphzzmzbawlfjfuvcfpwbqxvcyzhhuygjhhltgoteaznhvlkaaidqhzsfacoucwekerfmfzrhagpxrbxtlajsbezbgnwklcupvaeabviddxaxazqlbcddgcgoreacixudzyeavofanfxngqyhubmaftqyzqcinylowrotfvusctfijdsdggfnbxnbqsjfqwupokitgcmiwtthxlnfruvtsiuiafprbjgpuq",415)

print ret







     