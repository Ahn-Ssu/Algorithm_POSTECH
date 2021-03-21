import sys
import operator 
# from functools import reduce
# seq = tuple(map(int,sys.stdin.readline().split()))

# print(seq)

seq = (1,-2,3,-4,5,-3,8,-9,22)
print(seq)

max = operator.add(seq[0], seq[1])
max_idx = 0
length = 1

for idx in range(1,len(seq)-1,1):

    if max < (operator.add(seq[idx], seq[idx+1])):
        print("now sub max value",seq[idx] + seq[idx+1])
        max = operator.add(seq[idx], seq[idx+1])
        max_idx = idx
        print("now idx",idx)



for front in range(idx-1,0,-1):
    print(front)