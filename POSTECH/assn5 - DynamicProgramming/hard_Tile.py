import sys

T = int(sys.stdin.readline())
output = ""

input_list = [0] * T

for iteration in range(T):

    input_list[iteration] = int(sys.stdin.readline())


max_value = max(input_list)
seq = [0] * max_value

seq[0] = 2
seq[1] = 7
b1 = 7
b2 = 2
b3 = 2 

for o in range(3, max_value+1):
    way = 2*b1 + 3*b2 + b3 
    way = way%1234567890
    b3 += 2*b2
    b2 = b1
    b1 = way

    seq[o-1] = way


for one in input_list:
    output += "%s\n"%(seq[one-1])


print(output)