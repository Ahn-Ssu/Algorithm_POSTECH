import sys
import operator 



block_size = (2,4,8,16,32)
block_num = [10,10,10,10,10]
used = [0,0,0,0,0]

request_block = (5,5,5)


def stacking(block_size, request_block):

    print("----------in----------")
    print("in block_size : ", block_size)
    print("in request_block : ", request_block)

    n = len(block_size)

    if not block_size:
        return -1

    
    size = block_size[-1]
    able = ()
    for side in request_block:
        able += (side//size,)

    want =1 
    for k in able:
        want *= k

    print("want" ,want)
    print("used", used)
    print("block_num", block_num)
    
    if want==0:
        stacking(block_size[:-1], request_block)

    if block_num[n-1] > want :

        block_num[n-1] -= want
        used[n-1] += want

        

        usage = ()
        for axis in able:
            usage += (axis*size,)

        print("total usage :",usage)
        h = y = x = 0
        h = request_block[2] - usage[2]
        y = request_block[1] - usage[1]
        x = request_block[0] - usage[0]
        # h
        result = 1
        if h:
            print("h call",  (request_block[0],request_block[1],request_block[2] - usage[2]))
            result = stacking(block_size[:-1],(request_block[0],request_block[1],request_block[2] - usage[2]))
        
        if h == 0 :
            h = request_block[2]
        # y
        if y:
            print("y call", (request_block[0], y, request_block[0]))
            result = stacking(block_size[:-1], (request_block[0], y, h))
        
        if x:
            print("x call", (x, request_block[1], request_block[0]))
            result = stacking(block_size[:-1], (x, request_block[1], h))

        return result
    else:
        print("못넣어!")
        return -1

        


    
    

value = stacking(block_size, request_block)

if value == -1 :
    print(value)
else:
    for i in used:
        print(i, end=" s")