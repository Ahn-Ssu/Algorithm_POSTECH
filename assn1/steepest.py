import sys

def steepness(x1,x2,y1,y2):
    return abs(  (y2-y1)/ (x2-x1) )


def merge_sort(target_list):
    if len(target_list) <= 1:
        return target_list
    mid = len(target_list)//2
    left = merge_sort(target_list[:mid])
    right = merge_sort(target_list[mid:])
    return merge(left,right)
 
def merge(left, right):
    result = []
    while len(left) > 0 or len(right)>0:
        if len(left) > 0 and len(right) > 0:
 
            if left[0] <= right[0]:
                result.append(left[0])
                left=left[1:]
            else:
                result.append(right[0])
                right = right[1:]
 
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result
 
def find_point(point_list):
     
    max_s = 0 
    max_idx = 0

    for i in range(len(point_list)-1):

        now_s = steepness(point_list[i][0], point_list[i+1][0], point_list[i][1], point_list[i+1][1] )

        if now_s > max_s :
            max_s = now_s
            max_idx = i


    return max_idx


ans_list= []
stage = int(sys.stdin.readline())


for i in range(stage):
    input_num = int(sys.stdin.readline())
    case = []
    for i in range(input_num):
        
        # case.append(sys.stdin.readline().split())
        case.append(list(map(int, sys.stdin.readline().split())))

    sorted = merge_sort(case)

    final_idx = find_point(sorted)
    ans = "{} {} {} {}".format(sorted[final_idx][0], sorted[final_idx][1], sorted[final_idx+1][0], sorted[final_idx+1][1])
    ans_list.append(ans)

for ans in ans_list:
    print(ans)