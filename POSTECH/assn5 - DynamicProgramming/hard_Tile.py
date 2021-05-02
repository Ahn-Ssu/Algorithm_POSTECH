# import sys

# T = int(sys.stdin.readline())
# output = ""

# input_list = [0] * T

# for iteration in range(T):

#     input_list[iteration] = int(sys.stdin.readline())


# max_value = max(input_list)
# ans_list = [0] * T 


# b1 = 7
# b2 = 2
# b3 = 2 

# for o in range(3, max_value+1):
    
#     way = 2*b1 + 3*b2 + b3 
#     way = way%1234567890
#     b3 += 2*b2
#     b2 = b1
#     b1 = way


#     if o in input_list:
#         ans_list[input_list.index(o)] = way

# for idx, o in enumerate(input_list):
#     if o == 1 :
#         ans_list[idx] = 2
#         continue
#     if o == 2 :
#         ans_list[idx] = 2
#         continue
    


# for one in ans_list:
#     output += "%s\n"%(one)


# print(output)

def way(n):
    SIZE = 3
    ZERO = [[1, 0, 0], [0, 1, 0], [0,0,1]] 
    BASE = [[3, 1, -1], [1, 0,0], [0,1,0]] 

    # 두 행렬의 곱을 구한다
    def square_matrix_mul(a, b, size=SIZE):
        new = [[0 for _ in range(size)] for _ in range(size)]

        for i in range(size):
            for j in range(size):
                for k in range(size):
                    new[i][j] += a[i][k] * b[k][j]

        return new

    # 기본 행렬을 n번 곱한 행렬을 만든다
    def get_nth(n):
        matrix = ZERO.copy()
        k = 0
        tmp = BASE.copy()

        while 2 ** k <= n:
            if n & (1 << k) != 0:
                matrix = square_matrix_mul(matrix, tmp)
            k += 1
            tmp = square_matrix_mul(tmp, tmp)

        return matrix

    return get_nth(n)[1][0]


print(way(1))
