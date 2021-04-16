import heapq
# 기본적으로 최소힙만 제공함 
heap = []


heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
print(heap)

print(heapq.heappop(heap))
print(heap)


pre = [9,1,2,3,4,78,6]

heapq.heapify(pre)
print(pre)
print(heapq.heappop(pre))
print(pre)
print(heapq.heappop(pre))
print(pre)



# 최대힙으로 조정하기 
max_heap = []

for num in pre:
    heapq.heappush(max_heap,(-num, num))

print(max_heap)
print(heapq.heappop(max_heap))
print(max_heap)
print(heapq.heappop(max_heap))
print(max_heap)
print(heapq.heappop(max_heap))

heapq.heapify(dic)
pirnt(dic)