import math
import sys

def dist(x1,x2,y1,y2):
    return math.abs( (x2-x1) / (y2-y1) )


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
 
 
 
stage = int(sys.stdin.readline())
case = []

for i in range(stage):
    # case.append(sys.stdin.readline().split())
    case.append(list(map(int, sys.stdin.readline().split())))

sorted = merge_sort(case)
print(sorted)

