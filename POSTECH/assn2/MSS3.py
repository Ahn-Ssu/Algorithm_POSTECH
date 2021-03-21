import sys
import operator 
from functools import reduce
# seq = tuple(map(int,sys.stdin.readline().split()))


   # (1,-2,3,-4,5,-3,8,-9,22)
    # (-1,-2,-3,-4,-5)
    # (1,3,-1,2,4)
    # (1,-3,5,-7,10,-9,6,-4,2)
    # (4, -3, 5, -2, -1, 2, 6, -2)
seq = (4, -3, 5, -2, -1, 2, 6, -2)
n = len(seq) 

print("len", n)







max_element = seq[0] 

for one in seq:
    if operator.gt(one, max_element):
        max_element = one


local_sum = 0
max_sum = max_element 


start = 0 
for idx, one in enumerate(seq):
    local_sum = 0

    
    for o in seq[start:idx+1]:
        local_sum = operator.add(local_sum, o) 

    if operator.gt(0,local_sum):
        start = operator.add(idx,1)
        
    elif operator.gt(local_sum, max_sum ): 
        max_sum = local_sum

    # print("now start : ",start)
    # print("now idx : " , idx)
    # print("now local_sum :", local_sum)
    # print()


print(max_sum)