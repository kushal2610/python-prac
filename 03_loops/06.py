n = 0
factorial = 1
while n>=1:
    factorial = factorial*n
    n-=1
    if n == 0:
        n = 1
        break
    # print(factorial)
print(factorial)