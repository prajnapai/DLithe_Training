#Check if a number is prime or not

from math import sqrt

num = int(input())
f = 0
if num > 1:
    for i in range(2,int(sqrt(num))+1):
        if (num % i == 0):
            f = 1
            break
    if (f == 0):
        print(num,"is a prime number")
    else:
        print(num,"is not a prime number")
else:
    print("Enter a number greater than 1")


    


