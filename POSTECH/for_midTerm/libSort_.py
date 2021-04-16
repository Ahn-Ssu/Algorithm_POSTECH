
test = [[1,9,2,3,4,78,6],
[9,2,3,4,78,6],
[2,3,4,78,6],
[3,4,78,6]]

print(test)
test.sort()
print(test)

def second(x):
    return x[1]

test.sort(key=second)
print(test)
# test.sort(reverse=True)
# print(test)
