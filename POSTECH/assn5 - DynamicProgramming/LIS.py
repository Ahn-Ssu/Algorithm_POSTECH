import sys



T = int(sys.stdin.readline())


for interation in range(T):

    seq_len = int(sys.stdin.readline())
    seq = tuple(map(int,sys.stdin.readline().split()))

    # dir edge make 
    adj = []
    for i in range(seq_len):
        outgoing_edge = ()

        for j in range(i+1, seq_len):
            if seq[i] < seq[j] :
                outgoing_edge += (seq[j],)

        adj.append(outgoing_edge)
    # adj make end
    print(adj)
            