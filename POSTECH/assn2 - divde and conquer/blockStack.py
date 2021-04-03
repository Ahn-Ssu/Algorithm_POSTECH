import sys
import operator 

def stacking(block_size, request_block):

    # print("----------in----------")
    # print("in block_size : ", block_size)
    # print("in request_block : ", request_block)

    n = len(block_size)

    if not block_size:
        return -1

    
    size = block_size[-1]
    able = []
    for side in request_block:
        able += [side//size]

    want =1 
    for k in able:
        want = operator.mul(want, k)
    
    

    # print("want" ,want)
    # print("used", used)
    # print("block_num", block_num)
    
    if operator.eq(want,0):
        # print("want 0 call")
        return stacking(block_size[:-1], request_block)

    if operator.gt(block_num[n-1], 0) :

        if operator.ge(block_num[n-1], want):
            block_num[n-1] = operator.sub(block_num[n-1], want)
            used[n-1] = operator.add(block_num[n-1], want)

        else:
            # print("able",able)

            k = block_num[n-1]

            while 1 :
                multi = 1
                for i in range(len(able)):
                    multi = operator.mul(multi, able[i])
                    
                
                if operator.eq(multi, k) :
                    break
                else:
                    for i in range(len(able)):
                        if operator.ne(able[i], 1):
                            able[i] = operator.add(able[i], -1) 
                            break
            
            used[n-1] = operator.add(used[n-1],k)
            block_num[n-1] = 0

            # print("edited able",able)
            # able = [block_num[n-1],1,1]
            # used[n-1] += block_num[n-1]
            # block_num[n-1] = 0    

        # print("AFTER")
        # print("used", used)
        # print("block_num", block_num)

        

        usage = ()
        for axis in able:
            usage = operator.concat(usage, (operator.mul(axis,size),))
            

        # print("req :", request_block)
        # print("total usage :",usage)
        h = y = x = 0
        h = operator.sub(request_block[2], usage[2])
        y = operator.sub(request_block[1], usage[1])
        x = operator.sub(request_block[0], usage[0])
        # print("x : {} / y : {} / h : {}".format(x,y,h))

        
        # h
        result = 1
        if h:
            # print("h call", usage, (request_block[0],request_block[1],h))
            result = stacking(block_size[:-1],(request_block[0],request_block[1],h))
        # if h == 0 :
        #     h = usage[2]
        
        # y
        if y:
            # print("y call", usage, (request_block[0], y, usage[2]))
            result = stacking(block_size[:-1], (request_block[0], y, usage[2]))
        
        
        if x:
            # print("x call", usage,(x, request_block[1]-y, usage[2]))
            result = stacking(block_size[:-1], (x, request_block[1]-y, usage[2]))

        return result
    else:
        return stacking(block_size[:-1], request_block)
        

        



stage = int(sys.stdin.readline())
sizes = [0] * stage
blocks = [0] * stage
request = [0] * stage

for iteration in range(stage):
    sys.stdin.readline()

    sizes[iteration] = tuple(map(int,sys.stdin.readline().split()))
    blocks[iteration] = list(map(int,sys.stdin.readline().split()))
    request[iteration] = tuple(map(int,sys.stdin.readline().split()))

output = ""

for iteration in range(stage):

    block_size = sizes[iteration]
    block_num = blocks[iteration]
    used = [0] * len(block_size)

    request_block = request[iteration]

    # n = len(seq)

    result = stacking(block_size, request_block)

    if result == -1 :
        output += "%s\n"%result
    else:
        for i in used:
            output += "%s "%i
        
        output = output[:-1] +'\n'

    # output += "%s\n"%find_mss(seq, n)


print(output, end="")