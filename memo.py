import operator

usage = ()
usage += (1,)


usage = operator.concat(usage, (1,))
print(usage)