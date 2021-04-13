# list 사용
# 단순히 append(), pop(0)로 큐 동작
# 이게 내부 조정을 해야해서 항상 O(N) 타임을 2번 써먹음
# 인덱싱은 개빠름 
queue = [4,5,6]

print(queue)

queue.append(7)
queue.append(8)

print(queue)

print(queue.pop(0))
print(queue.pop(0))

print(queue)



#deque 사용
# appendleft(element), pop()
# 장점 내부가 linked list여서 insert/pop이 개빠름
# 대신 인덱싱은 느림
from collections import deque

queue = deque([4,5,6])

print(queue)
queue.appendleft(3)
queue.appendleft(2)
print(queue)

print(queue.pop())
print(queue.pop())
print(queue)


# 진짜 queue사용 
# put, get으로 동작
# 방향성 따로 없음 
# 근데 스레드용으로 보통 만듬
from queue import Queue
q = Queue()
print(q)
q.put(4)
q.put(5)
q.put(6)
print(q.get())
print(q.get())
print(q)