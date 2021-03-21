import sys
sys.setrecursionlimit(100000)
import operator 
from functools import reduce



def find_mss(target_seq, n):
    # print("-------in---------")
    # print("target_seq :",target_seq)
    # print("now n : ", n)


    if n == 1 : 
        # print("n==1 out")
        return target_seq[0]
    elif n == 2 :
        local_max = target_seq[0]
        
        for one in target_seq:
            if one > local_max:
                local_max = one
            
        if target_seq[0]+target_seq[1] > local_max:
            # print("n==2 out")
            return target_seq[0]+target_seq[1]
        else:
            # print("n==2 out")
            return local_max
    
    elif n == 3 :
        local_max = target_seq[0]

        for one in target_seq:
            if one > local_max:
                local_max = one
        
        for idx in range(n-1):
            if target_seq[idx]+target_seq[idx+1] > local_max:
                local_max = target_seq[idx]+target_seq[idx+1]
        # print("n==3 out")
        return local_max

    else:

        mid = int(n/2)
        
        # print("now seq :", target_seq)
        # print("now mid :",mid)
        leftMax = find_mss(target_seq[:mid], len(target_seq[:mid]))
        rigthMax = find_mss(target_seq[mid:], len(target_seq[mid:]))
        # center = find_mss(target_seq[mid:mid+1], 2)

        left_subMax = target_seq[mid-1]
        right_subMax = target_seq[mid]

        # print("mid :", mid)
        # print("left_subMax[mid] :", left_subMax)
        # print("right_subMax[mid] :", right_subMax)

        left_ss = 0
        right_ss = 0

        for one in target_seq[mid-1::-1]: #분기점을 포함하는 연속된 시퀀스의 최대 
            left_ss += one 
            if left_ss > left_subMax :
                left_subMax = left_ss

        for one in target_seq[mid:]:
            right_ss += one
            if right_ss > right_subMax:
                right_subMax = right_ss

        
        center = left_subMax + right_subMax 
        
        return max(center, leftMax, rigthMax)
        # if center > leftMax:
        #     if center > rigthMax:
        #         return center 
        
        # if leftMax > center:
        #     if leftMax > rigthMax:
        #         return leftMax 
            
        # if rigthMax > center:
        #     if rigthMax > leftMax:
        #         return rigthMax 
        




# seq = (1,-2,3,-4,5,-3,8,-9,22)

# n = len(seq) 
# print(find_mss(seq, n))
   # (1,-2,3,-4,5,-3,8,-9,22)
    # (-1,-2,-3,-4,-5)
    # (1,3,-1,2,4)
    # (1,-3,5,-7,10,-9,6,-4,2)
    # (4, -3, 5, -2, -1, 2, 6, -2)
# seq = (4, -3, 5, -2, -1, 2, 6, -2)

stage = int(sys.stdin.readline())
request = [0] * stage 

for iteration in range(stage):
    sys.stdin.readline()
    request[iteration] = tuple(map(int,sys.stdin.readline().split()))

output = ""

for seq in request:

    n = len(seq)
    output += "%s\n"%find_mss(seq, n)


print(output)