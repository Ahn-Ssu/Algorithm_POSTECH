def power(a, n):

    if n == 0 :
        return 1

    if n == 1 :
        return a 

    if n%2 == 0 :
        return power(a, n/2) * power(a)
    else:
        return power(a, (n-1)/2) * power(a, (n-1)/2) * a 


print(power(2,3))