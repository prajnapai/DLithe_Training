num = int(input())
number = num
reverse = 0
while (num > 0):
    remainder = num % 10
    reverse = reverse*10 + remainder
    num = num//10

if number == reverse:
    print(number,"Is a Palindrome")
else:
    print(number,"Not a Palindrome")