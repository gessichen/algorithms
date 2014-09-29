class Solution:
    # @param path, a string
    # @return a string

    def simplifyPath(self, path):
    	dirs = []
    	if path == '':
    		return ''
    	elif path == '/':
    		return '/'

    	dotcnt = 0
    	curdir = ''
    	dotasdir = False
    	preslash = False
    	for i in xrange (1, len(path)):
    		c = path[i]
    		if c != '/':
    			preslash = False
    			if c >= 'a' and c <= 'z':
    				if dotcnt > 0:
    					for i in xrange(0,dotcnt):
    						curdir += '.'
    					dotcnt = 0
    				curdir += c
    				print curdir
    			elif c == '.':
    				dotcnt += 1
    		else:
    			if preslash == False:
    				if dotcnt == 2 and curdir == '':
    					if len(dirs) > 0:
    						dirs.pop()
    				elif dotcnt >= 1 and curdir != '':
    					for i in xrange(0,dotcnt):
    						curdir += '.'
    				dirs.append(curdir)
    				curdir = ''
    				preslash = True
    				dotcnt = 0
    	print dirs
    	print dotcnt
    	
    	if curdir == '' and dotcnt == 2:
    		if len(dirs) > 0:
    			dirs.pop()
    	if dotcnt >= 1 and curdir != '':
    		for i in xrange(0,dotcnt):
    			curdir += '.'
    		dirs.append(curdir)
    	if dotcnt >= 3 and curdir == '':
    		print 'entered'
    		for i in xrange(0,dotcnt):
    			curdir += '.'
    		dirs.append(curdir)

    	wholepath = ''
    	for i in xrange(0,len(dirs)):
    		wholepath += '/'
    		wholepath += dirs[i]

    	if  wholepath == '':
    		wholepath = '/'
    	return wholepath

s = Solution()
simple = s.simplifyPath("/a/./b/../../c/")
print simple