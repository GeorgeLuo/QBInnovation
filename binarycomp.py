


## method returns bytecode of file
def getBytes(filename, numBytes):
	with open(filename, "rb") as binary_file:
		binary_file.seek(0)  # Go to beginning
		couple_bytes = binary_file.read(numBytes)
		return couple_bytes

## method returns bytecode of file
def getBytecode(filename):
	with open(filename, "rb") as binary_file:
	    # Read the whole file at once
	    data = binary_file.read()
	    return data

def bits(f):
    bytes = (ord(b) for b in f.read())
    for b in bytes:
        for i in xrange(8):
            yield (b >> i) & 1

def getSize(filename):
	with open(filename, "rb") as binary_file:
		binary_file.seek(0, 2)  # Seek the end
		return binary_file.tell()  # Get the file size

# returns array of mismatched byte indexes and number of mismatched bytes
def getMismatches(filename1, filename2):
	mismatchIndexes = []
	file1 = getBytecode(filename1)
	file2 = getBytecode(filename2)
	for index, byte in enumerate(file1):
		if byte != file2[index]:
			mismatchIndexes.append({index : byte})

	return {"mismatchIndexes" : mismatchIndexes, "numBytes" : len(mismatchIndexes)}

def reduceMismatches(mismatchDex):
	return 0




h = "testfiles/hellotest.doc"
h2 = "testfiles/hellotest2.doc"

print (getSize(h))
# print (getBytecode(h))
# print (getBytecode(h2))
print getMismatches(h, h2)