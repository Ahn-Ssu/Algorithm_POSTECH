import sys
sys.setrecursionlimit(100000)
import operator 
from functools import reduce
# seq = tuple(map(int,sys.stdin.readline().split()))


def find_front(target_idx):
    if operator.eq(target_idx, -1):
        return -1
    
    if operator.gt(seq[target_idx], 0): # seq[target_idx] > 0
        return target_idx
    else:
        return find_front(operator.add(target_idx, -1))
        
    
def find_back(target_idx, end):
    
    if operator.eq(target_idx, end):
        
        return -1

    if operator.gt(seq[target_idx], 0):
        return target_idx
    else:
        return find_back(operator.add(target_idx, 1), end)


stage = int(sys.stdin.readline())
request = [0] * stage 

for iteration in range(stage):
    sys.stdin.readline()
    request[iteration] = tuple(map(int,sys.stdin.readline().split()))
    

output = ""

# request = [(1,-2,3,-4,5,-3,8,-9,22), (-1,-2,-3,-4,-5), (1,3,-1,2,4),(1,-3,5,-7,10,-9,6,-4,2), (-1,-2,-3,4,22),(10,2,3)]
for seq in request:
    # print(seq)
    # (1,-2,3,-4,5,-3,8,-9,22)
    # (-1,-2,-3,-4,-5)
    # (1,3,-1,2,4)
    # (1,-3,5,-7,10,-9,6,-4,2)
    # seq = (1,-3,5,-7,10,-9,6,-4,2)
    # print(seq)
    
    
    max_value = seq[0]
    max_idx = 0
    length = 1

    for i  in range(len(seq)):
        if operator.gt(seq[i], max_value):
            max_value = seq[i]
            max_idx = i

    front = operator.add(max_idx, -1)
    back = operator.add(max_idx , length)
    seq_len = len(seq)

    while front >= 0 : 
        if operator.gt(seq[front], 0 ): # seq
            if reduce(operator.add, seq[front:max_idx+length]) > reduce(operator.add, seq[max_idx:max_idx+length]):
                max_idx = operator.add(max_idx, -1)
                length = operator.add(length, 1)
                front = operator.add(front, -1)
            else:
                front = operator.add(front, - 1)
            # 더한 후, 다음 친구도 검사할거임 
        else : # 0 보다 작은 경우 
            #지금 위치로부터, 양수 위치 찾아 주는 함수  있으면 인덱스, 없으면 -1 
            sub_idx = find_front(front)
            if operator.ne(sub_idx, -1):
                if(reduce(operator.add , seq[sub_idx:max_idx+length]) > reduce(operator.add, seq[max_idx:max_idx+length])):
                    length = operator.add(length, operator.sub(max_idx, sub_idx))
                    max_idx = sub_idx
                    front = operator.add(max_idx, -1)
                else:
                    front = operator.add(sub_idx, - 1)
            else:
                break


    while back < seq_len:
        if operator.gt(seq[back], 0):
            print(reduce(operator.add, seq[max_idx:back]))
            if reduce(operator.add, seq[max_idx:back]) > reduce(operator.add, seq[max_idx:max_idx+length]) :
                length = operator.add(length, 1)
                back = operator.add(back, 1)
            else:
                back = operator.add(back, 1)
        else:
            sub_idx = find_back(back, seq_len)
            if operator.ne(sub_idx, -1):
                if(reduce(operator.add , seq[sub_idx:back-1:-1]) > reduce(operator.add , seq[sub_idx:sub_idx-1:-1])  ):
                    length = operator.add(length, operator.sub(sub_idx, max_idx))
                    back = operator.add(max_idx, length)
                else:
                    back = operator.add(sub_idx, 1)
            else:
                break
    output += "%s\n"%reduce(operator.add , seq[max_idx:max_idx+length])


print(output, end="")