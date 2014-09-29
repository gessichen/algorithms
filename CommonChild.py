def commonChildLen (strA,strB):
	tA = posTable(strA)
	tB = posTable(strB)
	maxlen = 0
	for i in xrange (0,26):
		l =  compareCharactor (i,0,[],[],tA,tB)
		if l > maxlen:
			maxlen = l;
	return maxlen;

def insertPos(posA, posAlst, posB, posBlst, childlen):
	if len(posAlst) == 0:
		posAlst.append(posA)
		posBlst.append(posB)
		return True
	else:
		pa = 5000
		i = 0
		for i in xrange(0, len(posAlst)):
			if posA < posAlst[i]:
				pa = i
				break

		pb = 5000
		j = 0
		for j in xrange(0, len(posBlst)):
			if posB < posBlst[j]:
				pb = j
				break

		if (pa == pb):
			if pa < len(posAlst):
				posAlst.insert(pa,posA)
				posBlst.insert(pb,posB)	
			else:
				posAlst.append(posA)
				posBlst.append(posB)
			return True
		return False

def compareCharactor (index, childlen, posAlst, posBlst, tA, tB):
#	print posBlst
	print index
	if index == 26:
		print "26-------"
		return childlen
	c = str(chr(index + 65))
	if tA.has_key(c) and tB.has_key(c):
		posesInA = tA[c]
		posesInB = tB[c]
		maxlen = 0
		inserted = False
		for i in xrange(0, len(posesInA)):
			for j in xrange(0, len(posesInB)):
				inserted = insertPos (posesInA[i],posAlst,posesInB[j],posBlst,childlen)
				if inserted:
					childlen += 1
				ml = compareCharactor (index + 1, childlen, posAlst, posBlst, tA, tB)
				if ml > maxlen:
					maxlen = ml
				if inserted:
					posAlst.remove(posesInA[i])
					posBlst.remove(posesInB[j])
					childlen -= 1
		return maxlen
	else:
		return compareCharactor(index + 1, childlen,posAlst, posBlst, tA, tB)


def posTable (s):
	dic = {}
	for i in xrange (0 ,len(s)):
		c = s[i]
		if dic.has_key (c):
			poslst = dic[c]
			poslst.append(i)
		else:
			dic[c] = [i]
#	print dic
	return dic

A = "APMCTKBUKYRGZPAUVZEBVUXRGDVITOYXWQWRVCSXESMEHQLHPDJQWETAWQVSBRRNRRFDLFTRXOTKQHFTYAZSGBORDNAMUAJTPVOKERLVOLEALDQQLUDCUIRXJHQEZBRWYPFJXNTPELEZHNJILIZVZLYQJDFYSYQNRFFAOYXHQBQVRLFDIIOGWKQIZGVELYOUKZBKMHVYGIKIPSEMWSCWYOJTHOQKMLBAIZYNAKYNCXKDTTESODDAEAHKCDHCJYAHERACMLYQHXIRDFUSRTZDNVHSYFKCSPPYSLHOGIBTNUJTZQWVTHKUNDNWZADMATSUXEISCACQNQXIHNTXGCZUGIGBDONYTUXAXFINAYGZJVDCTZCWPGFNQDPERUCNJUXIFDSQHULYPZRNUOKMLMMQAJMLKCHJMEFJVRYZIPFQOBSDPAITHGMNKROCWJEGESCGOIUOQHOYUEQNPJPBMCNRZUHOSQNSUNCSTVQVWFGMUFJZGMEUVUPH"
B = "JUVSDRRSHFGSSLLLZEPJDVAWDPKQBKUHHOZFFXKQMGAACZUYOMNPHWGTYZWQGSMNYXWNFYNOIVVMPZXUNKJQYBYJINBOHXUWIVRTVLEKCOPDMTKTGDBWECDAVPMLHQLERZHDVZJZODPSAPGSRWJXNGFEBQBLTLNDIEGFHEGHJWFOIYXRUJMODSNXUFWBIJJMXTFMUKQEYPNBTZFEJNLDNWCGQLVUQUKGZHJOKZNPMUYEQLEYNNORKJQAMSTHTBCCPQTTCPRZATWNJQJXPODRXKIWDOFUBZVSDTAPFRMXJBJMUGVRZOCDUIPXVEGMRQNKXDKNWXMTNDJSETAKVSYMJISAREEJPLRABMXJSRQNASOJNEEVAMWCFJBCIOCKMHCMYCRCGYFNZKNALDUNPUSTSWGOYHOSWRHWSMFGZDWSBXWXGVKQPHGINRKMDXEVTNNZTBJPXYNAXLWZSBUMVMJXDIKORHBIBECJNKWJJJSRLYQIKKPXSNUT"

l = commonChildLen (A,B)
print str(l)