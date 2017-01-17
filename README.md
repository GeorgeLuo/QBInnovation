# QBInnovation

## Some data engineering modules

pattern_find.py contains the important method testWindows(maxSeqLength, byteIndexes). This searches through an array of integers and finds simple patterns.

Example:

when maxSeqLength = 5, the method detects for patterns of [...n, n+m, n+2m, n+3m...] for values of m < or equal to 5 within byteIndexes.

for arr = [11,12,13,14,15,16,17,20,23,26,27,28,29,30,35,40,45], the patterns detected are [11,12,13,14,15,16,17], [17,20,23,26], [27,28,29,30], and [30,35,40,45]. The solution is provided in a dictionary format, 

```
[{'start': 13, 'sequence_length': 5, 'sequence': [30, 35, 40, 45]}, 
{'start': 6, 'sequence_length': 3, 'sequence': [17, 20, 23, 26]}, 
{'start': 0, 'sequence_length': 1, 'sequence': [11, 12, 13, 14, 15, 16, 17]}, 
{'start': 9, 'sequence_length': 1, 'sequence': [26, 27, 28, 29, 30]}]
```
Where start is the index of the first value of a sequence and sequence_length is the period of the sequence.

genSequence(chg, root) takes a chg object and makes changes to array root.

Example:

when,
chg = {"startIndex" : 0, "endIndex" : 4, "sequence" : 2, "bytes" : ['111', '101', '111', '011', '001']}
root = ['0','0','0','0','0','0','0','0']

genSequence returns,
['111', '0', '101', '0', '111', '0', '011', '0']

