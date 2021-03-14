import sys

def find_loc(vli_list):
    # odd
    if len(vli_list)%2 == 1 :
        spot = vli_list[len(vli_list)//2]
    #even
    else:
        left_p = vli_list[len(vli_list) //2 -1]
        right_p = vli_list[len(vli_list) // 2]

        left = 0
        right = 0 

        for vli in vli_list:
            if vli != left_p:
                left += abs(left_p - vli)
        
        for vli in vli_list:
            if vli != right_p:
                right += abs(left_p - vli)

        # 두 지점 중 더 작은 값의 위치
        if left > right :
            spot = right_p
        else:
            spot = left_p

    sum = 0 

    for vli in vli_list:
        if vli != spot:
            sum += abs(spot - vli)
    
    return sum

            

stage = int(sys.stdin.readline())
case = []

for i in range(stage*2):
    case.append(sys.stdin.readline())

for i in range(stage):
    vli_list = list(map(int, case[i*2+1].split()))
    print(find_loc(vli_list))
