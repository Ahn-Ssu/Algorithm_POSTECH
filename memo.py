

li = [list()*5]
print(li)

li = []
for i in range(5):
    print(id(list()))
    li.append(list())
    
print(li)

for idx, i in enumerate(li):
    print(id(i))

    i.append(idx)


print(li)

