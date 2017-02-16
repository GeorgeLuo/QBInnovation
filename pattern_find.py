from __future__ import print_function
import math

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
					print (byteIndexes[begIndex:j])
					if last_found != None:
						if byteIndexes[begIndex:(j - 1)] == last_found:
							ret.pop()
					ret.append({"sequence" : byteIndexes[begIndex:j], "start" : begIndex, "sequence_length" : i})
					start = begIndex
					end = j
					last_found = byteIndexes[begIndex:j]
	return ret

# returns array of substring permutations of input string
from itertools import permutations
def get_substrings(input_text):
	return set([''.join(p) for p in permutations(input_text)])

# return x by y matrix with default_data in every location
def x_by_y_matrix(x, y, default_data):
	return [[default_data for a in xrange(0,x)] for b in xrange(0,y)]

# print(x_by_y_matrix(4,5,'hello'))
# print (get_substrings('quandary'))
# print (genSequence(chg, root))
# print(testWindows(5, mem))

import random

# pow(x,y,z) = (x^y) % z

# use Python 3 print function
# this allows this code to run on python 2.x and 3.x

from Crypto.Util import number

n_length = 2048

 
# Variables Used


sharedPrime = int('0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD1'
         '29024E088A67CC74020BBEA63B139B22514A08798E3404DD'
         'EF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245'
         'E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7ED'
         'EE386BFB5A899FA5AE9F24117C4B1FE649286651ECE65381'
         'FFFFFFFFFFFFFFFF', 0)

# sharedPrime = int('0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67'
#             'CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF2'
#             '5F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6'
#             'F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007C'
#             'B8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62'
#             'F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32'
#             '905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9'
#             'DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AAAC4'
#             '2DAD33170D04507A33A85521ABDF1CBA64ECFB850458DBEF0A8AEA71575D06'
#             '0C7DB3970F85A6E1E4C7ABF5AE8CDB0933D71E8C94E04A25619DCEE3D2261A'
#             'D2EE6BF12FFA06D98A0864D87602733EC86A64521F2B18177B200CBBE11757'
#             '7A615D6C770988C0BAD946E208E24FA074E5AB3143DB5BFCE0FD108E4B82D1'
#             '20A92108011A723C12A787E6D788719A10BDBA5B2699C327186AF4E23C1A94'
#             '6834B6150BDA2583E9CA2AD44CE8DBBBC2DB04DE8EF92E8EFC141FBECAA628'
#             '7C59474E6BC05D99B2964FA090C3A2233BA186515BE7ED1F612970CEE2D7AF'
#             'B81BDD762170481CD0069127D5B05AA993B4EA988D8FDDC186FFB7DC90A6C0'
#             '8F4DF435C93402849236C3FAB4D27C7026C1D4DCB2602646DEC9751E763DBA'
#             '37BDF8FF9406AD9E530EE5DB382F413001AEB06A53ED9027D831179727B086'
#             '5A8918DA3EDBEBCF9B14ED44CE6CBACED4BB1BDB7F1447E6CC254B33205151'
#             '2BD7AF426FB8F401378CD2BF5983CA01C64B92ECF032EA15D1721D03F482D7'
#             'CE6E74FEF6D55E702F46980C82B5A84031900B1C9E59E7C97FBEC7E8F323A9'
#             '7A7E36CC88BE0F1D45B7FF585AC54BD407B22B4154AACC8F6D7EBF48E1D814'
#             'CC5ED20F8037E0A79715EEF29BE32806A1D58BB7C5DA76F550AA3D8A1FBFF0'
#             'EB19CCB1A313D55CDA56C9EC2EF29632387FE8D76E3C0468043E8F663F4860'
#             'EE12BF2D5B0B7474D6E694F91E6DCC4024FFFFFFFFFFFFFFFF', 0)

sharedBase = 2      # g
 
aliceSecret = 32     # a
bobSecret = 54      # b
 
# Begin
print( 'Publicly Shared Variables:')
print( 'Publicly Shared Prime: ', sharedPrime)
print( 'Publicly Shared Base:  ', sharedBase )
 
# Alice Sends Bob A = g^a mod p
A = pow(sharedBase, aliceSecret, sharedPrime) # (sharedBase**aliceSecret) % sharedPrime
print( 'Alice Sends Over Public Chanel: ', A )
 
# Bob Sends Alice B = g^b mod p
B = pow(sharedBase, bobSecret, sharedPrime)
print('Bob Sends Over Public Chanel: ', B )
 
print( 'Privately Calculated Shared Secret: ' )
# Alice Computes Shared Secret: s = B^a mod p
aliceSharedSecret = pow(B, aliceSecret, sharedPrime)
print( 'Alice Shared Secret: ', aliceSharedSecret )
 
# Bob Computes Shared Secret: s = A^b mod p
bobSharedSecret = pow(A, bobSecret, sharedPrime)
print( 'Bob Shared Secret: ', bobSharedSecret )





