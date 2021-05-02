import sys

T = int(sys.stdin.readline())
output = ""
for interation in range(T):

    seq_len = int(sys.stdin.readline())
    seq = tuple(map(int,sys.stdin.readline().split()))

    # for record subSeq. lenght
    L = [0] * seq_len

    # adj make
    ## 1) linked list format
    # adj = []
    # for i in range(seq_len):
    #     outgoing_edge = ()

    #     for j in range(i+1, seq_len):
    #         if seq[i] < seq[j] :
    #             outgoing_edge += (seq[j],)

    #     adj.append(outgoing_edge)
    ## linked adj make end
    
    ## 2)matrix format
    adj = []

    for i in range(seq_len):

        outgoing_edge = [0] * seq_len

        for j in range(i+1, seq_len):
            if seq[i] < seq[j] :
                outgoing_edge[j] = 1
        
        adj.append(outgoing_edge)
    ## end - matrix adj


    
    for idx in range(seq_len):

        # find max value in incomming
        temp_L_max = 0
        # seq_len-1 : last node is sink
        # 0 to idx-1 : directed and no self-loopBackk
        for column in range(idx):
            # print("idx : {} | column : {}".format(idx, column))
            # print("adj[idx] ", adj[idx])
            # print("adj[idx][column]", adj[idx][column])
            # print("adj[column][idx]", adj[column][idx])
            if adj[column][idx] == 1 :
                temp_L_max = max(temp_L_max, L[column])
        
        L[idx] = temp_L_max + 1
        # print("\tL :",L)
    
    output += "%s\n"%max(L)
print(output)