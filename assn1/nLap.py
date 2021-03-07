from collections import OrderedDict

stage = input()





# print(list(OrderedDict.fromkeys(b)))
# print(set(b))


# for one in record:
#     print(b)
#     b.remove(one)
#     print(b)
#     print()


# print(first[-1]) # ㅁㅏ지막꺼 출력 

def lim (record_seq):
    print("now record", record)

    if len(record_seq) == 0:
        print("NO")
        return 
    
    record.append(list(OrderedDict.fromkeys(record_seq)))

    print("전",record_seq)
    for lap in record[-1]:
        record_seq.remove(lap)

    print("후",record_seq)
    print()

    if record[0] != record[-1]:
        print("YES")
        return

    lim(record_seq)

for i in range(stage):
    
    n, c = map(int, input().split())
    s = input().split()
    record = []
    lim(b)