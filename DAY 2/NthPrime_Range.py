#Find the Nth prime number in a given range

from math import sqrt

start = int(input())
end = int(input())
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

def nthPrime(start,end,n):
    count = 0
    for i in range(start,end+1):
        if isPrime(i):
            count +=1
            if count == n:
                return i

res = nthPrime(start,end,num)
print(res)


