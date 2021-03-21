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
        center = find_mss(target_seq[mid:mid+1], 2)

        # center 가 제일 큰 경우 
        if center > leftMax:  # 경계에 위치한 친구들이 제일 큰 경우 그 친구들 리턴
            if center > rigthMax:
                return center
        
        if center > rigthMax: # 경계에 위치한 친구들이 제일 큰 경우 그 친구들 리턴
            if center > leftMax:
                return center 

        # 왼쪽이 제일 큰 경우 
        if leftMax > rigthMax :

            #오른쪽의 합이 중앙의 뺏긴 값보다 크면 오른쪽이랑 더해서 리턴
            # 작으면 뺏긴 값 체크 
            

            # 경계에 뺏긴 값이 양수인지 확인
            if target_seq[mid+1] > 0 : 
                return leftMax + target_seq[mid+1] # 양수면 더해서 리턴
            else :
                return leftMax # 아니면 걍 리턴  
