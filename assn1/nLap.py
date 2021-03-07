from collections import OrderedDict

stage = int(input())
case = []

for i in range(stage):
    n_c = input()
    seq = input().split()
    case.append(seq)


def lim (record_seq):
    if len(record_seq) == 0:
        print("NO")
        return 
    
    record.append(list(OrderedDict.fromkeys(record_seq)))

    for lap in record[-1]:
        record_seq.remove(lap)

    if record[0] != record[-1]:
        print("YES")
        return

    lim(record_seq)

for i in range(stage):
    record =  []
    lim(case[i])