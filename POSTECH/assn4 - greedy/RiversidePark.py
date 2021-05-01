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

    print(info)
    print(tuple(set(info)))
                

print(output)