import sys
sys.setrecursionlimit(100000)
import operator 
from functools import reduce
# seq = tuple(map(int,sys.stdin.readline().split()))

seq = (1,-3,5,-7,10,-9,6,-4,2)
n = len(seq) 



def find_mss(target_seq, n):

    if n == 1 : 
        return target_seq
    elif n == 2 :
        local_max = target_seq[0]

        for 