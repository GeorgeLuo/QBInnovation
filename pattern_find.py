chg = {"startIndex" : 0, "endIndex" : 4, "sequence" : 2, "bytes" : ['111', '101', '111', '011', '001']}

root = ['','','','','','','','']

def genSequence(chg, root):
	ret = root[:]
	seq = chg['sequence']
	start = chg['startIndex']
	end = chg['endIndex']
	bytes = chg['bytes']
	for byte in bytes:
		if start < len(ret):
			ret[start] = byte
			start = start + seq
		else:
			break
	return ret
	
arr = [11,12,13,14,15,16,17,20,23,26,27,28,29,30,35,40,45]

# check if byteIndexes contains sequence of seqLength
def isSequence(seqLength,byteIndexes):
	if len(byteIndexes) < 3:
		return False
	start = byteIndexes[0]
	end = byteIndexes[len(byteIndexes)-1]
	l = range(end + 1)
	if (end - start)%seqLength != 0:
		return False
	if l[start::seqLength] == byteIndexes:
		return True
	else:
		return False

# find patterns of period <= maxSeqLength
def testWindows(maxSeqLength, byteIndexes):
	# if isSequence is false, start at next min length
	ret = []
	last_found = None
	start = 0
	end = 0
	for i in range(maxSeqLength,0,-1):
		for begIndex in range(0, len(byteIndexes)):
			for j in range(begIndex + 2, len(byteIndexes) + 1):
				if isSequence(i, byteIndexes[begIndex:j]) and not ((start <= begIndex) and (end >= j)):
					print byteIndexes[begIndex:j]
					if last_found != None:
						if byteIndexes[begIndex:(j - 1)] == last_found:
							ret.pop()
					ret.append({"sequence" : byteIndexes[begIndex:j], "start" : begIndex, "sequence_length" : i})
					start = begIndex
					end = j
					last_found = byteIndexes[begIndex:j]
	return ret

print (genSequence(chg, root))
print(testWindows(5, arr))



