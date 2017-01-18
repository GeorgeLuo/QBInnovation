chg = {"startIndex" : 0, "endIndex" : 4, "sequence" : 2, "bytes" : ['111', '101', '111', '011', '001']}

root = ['','','','','','','','']

mem = [540, 588, 2104, 2106, 2108, 2110, 2112, 2114, 2116, 2118, 2120, 2122, 2124, 2126, 2128, 2130, 2132, 2134, 2136, 2138, 2140, 2142, 2144, 2146, 2148, 2150, 2152, 2154, 2156, 2158, 2160, 2568, 2569, 2572, 2573, 2576, 2577, 2578, 3030, 3031, 3032, 3033, 3035, 3036, 3037, 3039, 3040, 3041, 3044, 3045, 3046, 3047, 3049, 3050, 3051, 3053, 3054, 3055, 3071, 3080, 3081, 3084, 3085, 3088, 3101, 3114, 3450, 3453, 3454, 3455, 3457, 3458, 3459, 3460, 3461, 3462, 3463, 3464, 3465, 3466, 3467, 3468, 3469, 3470, 3471, 3472, 3473, 3474, 3475, 3476, 3477, 3478, 3479, 3480, 3481, 3494, 3497, 3498, 3499, 3501, 3502, 3503, 3504, 3505, 3506, 3507, 3508, 3509, 3510, 3511, 3512, 3513, 3514, 3515, 3516, 3517, 3518, 3519, 3520, 3521, 3522, 3523, 3524, 3525, 3583, 3588, 4774, 4794, 4806, 4818, 4835]

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
print(testWindows(5, mem))



