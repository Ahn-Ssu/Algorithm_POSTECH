import sys
sys.setrecursionlimit(100000)
import operator 
from functools import reduce
# seq = tuple(map(int,sys.stdin.readline().split()))

seq = (1,-3,5,-7,10,-9,6,-4,2)
n = len(seq) 



def find_mss(target_seq, n):

    if n == 1 : 
        return target_seq[0]
    elif n == 2 :
        local_max = target_seq[0]

        for one in target_seq:
            if one > local_max:
                local_max = one
            
        if target_seq[0]+target_seq[1] > local_max:
            return target_seq[0]+target_seq[1]
        else:
            return local_max
    
    elif n == 3 :
        local_max = target_seq[0]

        for one in target_seq:
            if one > local_max:
                local_max = one
        
        for idx in range(len(n-1)):
            if target_seq[idx]+target_seq[idx+1] > local_max:
                local_max = target_seq[idx]+target_seq[idx+1]
        
        return local_max

    else:

        mid = n/2

        leftMax = find_mss(target_seq[:mid], mid)
        rigthMax = find_mss(target_seq[mid+1:], mid)
        # center = find_mss(target_seq[mid:mid+1], 2)

        if leftMax > rigthMax :
            if target_seq[mid+1] > leftMax :
                return find_mss(target_seq[mid:mid+1], 2)
            elif target_seq[mid+1] > 0 :
                return leftMax + target_seq[mid+1]
            else:
                return leftMax
        
        
             
        
            
        

        
