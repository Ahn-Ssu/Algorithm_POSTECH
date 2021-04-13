
testCase = [5,3,8,4,9,1,6,2,7]
#[10,5,8,7,8,4,3,2,9]

print(testCase)



pivot = testCase[0]
low = 1
high = len(testCase)-1
print("pivot : {}".format(pivot))
print("low idx: {}".format(low))
print("high idx: {}".format(high))



def quick_sort(arr): #쉬운버전

    if len(arr) <= 1: #baseCase, len 1
        return arr
    

    pivot = arr[len(arr) // 2] #center pivot

    #매번 재귀 호출될 때 마다 새로운 리스트를 생성하기 때문에 메모리 사용 측면에서 조금 비효율 적
    lesser_arr, equal_arr, greater_arr = [], [], [] # 같은 것, 작은것, 큰 것
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)

            # 구조 자체를 자기보다 작은 것들을 우측에, 큰것은 좌측에 둠 
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)


def quick_sort2(arr):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high) # mid point를 받아서, 왼쪽과 오른쪽에 대해서 recursive
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]  # 피봇의 위치 센터 

        while low <= high: # 하이가 로우보다 앞에 있을 때 까지 
            while arr[low] < pivot: # arr[low] 중에 현재 피봇보다 큰 친구를 찾아냄 
                low += 1
            while arr[high] > pivot: # arr[high]를 통해 현재 피봇보다 작은 친구를 찾아냄 
                high -= 1

            if low <= high: # 아직 하이랑 로우가 교차하지 않았다면
                arr[low], arr[high] = arr[high], arr[low] # 찾아낸 친구들을 스왑
                low, high = low + 1, high - 1
        return low # 얘는 high나 low 중 교차한 지점에서 low를 리턴함 

    return sort(0, len(arr) - 1)