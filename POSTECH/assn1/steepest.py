import sys

def steepness(x1,x2,y1,y2):
    return abs(  (y2-y1)/ (x2-x1) )


# def merge_sort(target_list):
#     if len(target_list) <= 1:
#         return target_list
#     mid = len(target_list)//2
#     left = merge_sort(target_list[:mid])
#     right = merge_sort(target_list[mid:])
#     return merge(left,right)

# def merge(left, right):
#     result = []
#     while len(left) > 0 or len(right)>0:
#         if len(left) > 0 and len(right) > 0:
 
#             if left[0] <= right[0]:
#                 result.append(left[0])
#                 left=left[1:]
#             else:
#                 result.append(right[0])
#                 right = right[1:]
 
#         elif len(left) > 0:
#             result.append(left[0])
#             left = left[1:]
#         elif len(right) > 0:
#             result.append(right[0])
#             right = right[1:]
#     return result

def quick_sort(arr):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    return sort(0, len(arr) - 1)

def find_point(point_list):
     
    max_s = 0 
    max_idx = 0

    for i in range(len(point_list)-1):

        now_s = steepness(point_list[i][0], point_list[i+1][0], point_list[i][1], point_list[i+1][1] )

        if now_s > max_s :
            max_s = now_s
            max_idx = i


    return max_idx


stage = int(sys.stdin.readline())
ans_list= [0] * stage

for iter in range(stage):
    input_num = int(sys.stdin.readline())
    case = [0] * input_num
    for i in range(input_num):
        
        # case.append(sys.stdin.readline().split())
        # case.append(list(map(int, sys.stdin.readline().split())))
        case[i] = list(map(int, sys.stdin.readline().split()))

    # sorted = merge_sort(case)
    sorted = quick_sort(case)
    # print(case)

    final_idx = find_point(case)
    # ans = "{} {} {} {}".format(sorted[final_idx][0], sorted[final_idx][1], sorted[final_idx+1][0], sorted[final_idx+1][1])
    ans = "%s %s %s %s" % (case[final_idx][0], case[final_idx][1], case[final_idx+1][0], case[final_idx+1][1])
    # f_str = "f'{" + '}{'.join([f'x{i}' for i in range(num_vars)]) + "}'"
    ans_list[iter] = ans

output = ""
for ans in ans_list:
    output += ans +'\n'
print(output)