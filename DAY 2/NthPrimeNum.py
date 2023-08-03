#Find the Nth prime number
from math import sqrt

num = int(input())

def isPrime(num):
    f = 0
    if num > 1:
        for i in range(2,int(sqrt(num))+1):
            if (num % i == 0):
                f = 1
                break
        if (f == 0):
            return True
        else:
            return False
    else:
        return False

def nthPrime(num):
    count = 0
    n = 2
    while count < num:
        if isPrime(n):
            count += 1
        n += 1
    return n - 1

res = nthPrime(num)
print(res)


