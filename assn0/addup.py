size = int(input())

output = [] 

for i in range(size) :
    a,b = map(int, input().split())
    output.append(a+b)

for i in output:
    print(i)
