# -*- coding: utf-8 -*-
import sys
import heapq



stage = int(sys.stdin.readline())

for i in range(stage):
    amp_n, now_range, goal = map(int,sys.stdin.readline().split())

    amp_list = [0]*stage
    
    for k in range(amp_n):
        amp_info = tuple(map(int,sys.stdin.readline().split()))

        amp_list[k]=amp_info

    amp_list.sort() # 거리 순으로 정렬

    # 현재 사거리 까지 줍줍 -> Q에 넣음
    # Q에는 파워의 세기를 순서대로 넣음 
    # 사거리 닿을때까지 Q 에 넣음 
    # Q를 초기화 하지 않아도 됨 

    h = []
    amp_count = 0 
    while amp_list: # amp_list의 끝까지 회전


        checked_idx = 0 # 어디까지 확인 했는지 기록
        
        for idx, (amp_loca, amp_power) in enumerate(amp_list):

            checked_idx = idx
            if amp_loca <= now_range: # 사거리안에 amp가 위치하면 Q에 저장 
                heapq.heappush(h, -amp_power) # 음수 붙여서 max Q로 활용
            else :
                # 더 이상 사거리에 있는 친구들이 없음
                break
        
        if not h and (now_range<goal): # 힙에서 더이상 꺼낼거 없고, 목표 사거리 달성 못한 경우
            print(-1)
            break

        
        now_range += heapq.heappop(h)*(-1)
        amp_count += 1 
        # print(now_range)

        if now_range >= goal:
            print(amp_count)
            break

        amp_list = amp_list[checked_idx:] #이미 확인해서 q에 담긴 친구들은 리스트에서 제거 



am_n, now_range, goal = (2,4,14)

amp_list = [
    (2, 3),
    (4, 7)
]

