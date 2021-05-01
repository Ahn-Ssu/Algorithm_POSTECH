# -*- coding: utf-8 -*-
import sys
import operator 
import heapq



stage = int(sys.stdin.readline())
output = ""
for i in range(stage):
    amp_n, now_range, goal = map(int,sys.stdin.readline().split())

    amp_list = []
    
    for k in range(amp_n):
        amp_info = tuple(map(int,sys.stdin.readline().split()))

        heapq.heappush(amp_list, amp_info)

        # amp_list[k] = amp_info

    # amp_list.sort() # 거리 순으로 정렬

    # 현재 사거리 까지 줍줍 -> Q에 넣음
    # Q에는 파워의 세기를 순서대로 넣음 
    # 사거리 닿을때까지 Q 에 넣음 
    # Q를 초기화 하지 않아도 됨 

    h = []
    amp_count = 0 
    while amp_list: # amp_list의 끝까지 회전

        while amp_list:
            if operator.le(amp_list[0][0] , now_range):

                if operator.ge(operator.add(now_range , amp_list[0][1]) , goal): # 입력이 정렬되고 힙이 망가질때의 대비;
                    # now_range += amp_list[0][1]
                    # amp_count += 1
                    temp = heapq.heappop(amp_list)
                    heapq.heappush(h, (-temp[1],temp[1]))
                    break

                temp = heapq.heappop(amp_list)
                heapq.heappush(h, (-temp[1],temp[1]))
            else:
                # 일단 현재 사거리에 있는 친구들을 다 주움 
                break 

        # if now_range >= goal:
        #     output += "%s\n"%amp_count
        #     break

        if operator.and_(operator.not_(h), (operator.lt(now_range, goal))): # 힙에서 더이상 꺼낼거 없고, 목표 사거리 달성 못한 경우
            output += "%s\n"%-1
            break

        while h:    
            # now_range = operator.add(now_range, operator.neg(heapq.heappop(h)))
            now_range = operator.add(now_range, heapq.heappop(h)[1])
            amp_count = operator.add(amp_count, 1 )

            if operator.ge(now_range, goal):
                output += "%s\n"%amp_count
                break
        

        if operator.ge(now_range, goal):
                # output += "%s\n"%amp_count
                break

        if operator.not_(h):
            if amp_list:
                continue
            else:
                break
print(output)