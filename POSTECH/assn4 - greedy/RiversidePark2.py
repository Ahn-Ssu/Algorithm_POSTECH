import sys

stage = int(sys.stdin.readline())
output = ""

for i in range(stage):
    house_num, city_width = map(int,sys.stdin.readline().split())

    info = [0]*city_width
    for j in range(house_num):
        house_info = tuple(map(int,sys.stdin.readline().split()))

        for k in range(house_info[0], house_info[1]):
            info[k] = house_info[2]

    stack = []
    max_size = 0 #min(info) * city_width

    for idx, h in enumerate(info):
        before_idx = 0
        while stack and stack[-1][0] > h:
            
            last = stack.pop()
            before_idx = last[1]
            temp_ = (idx - last[1]) * last[0]

            if max_size < temp_:
                max_size = temp_

            if not stack:
                break

        if not stack:
            stack.append((h, before_idx)) 
        if stack[-1][0] < h:
            stack.append((h, before_idx)) 

    while stack:
        last = stack.pop()

        temp_ = (city_width - last[1]) * last[0]

        if max_size < temp_:
            max_size = temp_


    output = output + "%s\n"%max_size
                

print(output)