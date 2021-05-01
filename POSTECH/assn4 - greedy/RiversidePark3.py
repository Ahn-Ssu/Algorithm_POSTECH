import sys

stage = int(sys.stdin.readline())
output = ""

for i in range(stage):
    house_num, city_width = map(int,sys.stdin.readline().split())

    info = [0]*house_num

    stack = []
    max_size = 0 

    for j in range(house_num):
        info[j] = list(map(int,sys.stdin.readline().split()))
        
    
    for hull in info:
        # print("now hull", hull)

        if not stack:
            stack.append(hull)
            continue


        while stack and stack[-1][2] > hull[2]: # 들어온 친구가 높이가 더 낮음 

            temp_hull = stack.pop()
            

            temp_a = (hull[0] - temp_hull[0]) * temp_hull[2]

            # print("stack",stack)
            # print("temp hull",temp_hull)
            # print("ta",temp_a)

            if temp_a > max_size:
                max_size = temp_a
        
        if stack:
            hull[0] = stack[-1][1]
        else:
            hull[0] = 0

        stack.append(hull)

            



    while stack :
        temp_hull = stack.pop()

        if stack:
            w = city_width - stack[-1][1]
        else:
            w = city_width
        # print("end point")
        # print("w", w)
        # print("a", w*temp_hull[2])

        if w*temp_hull[2] > max_size:
            max_size = w*temp_hull[2]



                


    output = output + "%s\n"%max_size
    # print()
                

print(output)